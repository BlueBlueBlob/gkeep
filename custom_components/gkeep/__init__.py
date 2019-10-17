"""
Component to integrate with blueprint.

For more details about this component, please refer to
https://github.com/custom-components/blueprint
"""
import os
from datetime import timedelta
import logging
import voluptuous as vol
from homeassistant import config_entries
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers import discovery
from homeassistant.util import Throttle

import gkeepapi

from integrationhelper.const import CC_STARTUP_VERSION

from .const import (
    CONF_PASSWORD,
    CONF_USERNAME,
    CONF_DEFAULT_LIST,
    DEFAULT_NAME,
    DOMAIN_DATA,
    DOMAIN,
    ISSUE_URL,
    PLATFORMS,
    REQUIRED_FILES,
    VERSION,
)

MIN_TIME_BETWEEN_UPDATES = timedelta(seconds=300)

_LOGGER = logging.getLogger(__name__)


CONFIG_SCHEMA = vol.Schema(
    {
        DOMAIN: vol.Schema(
            {
                vol.Optional(CONF_USERNAME): cv.string,
                vol.Optional(CONF_PASSWORD): cv.string,
            }
        )
    },
    extra=vol.ALLOW_EXTRA,
)


async def async_setup(hass, config):
    """Set up this component using YAML."""

    # Check that all required files are present
    file_check = await check_files(hass)
    if not file_check:
        return False

    return True


async def async_setup_entry(hass, config_entry):
    """Set up this integration using UI."""
    conf = hass.data.get(DOMAIN_DATA)
    if config_entry.source == config_entries.SOURCE_IMPORT:
        if conf is None:
            hass.async_create_task(
                hass.config_entries.async_remove(config_entry.entry_id)
            )
        return False

    # Print startup message
    _LOGGER.info(
        CC_STARTUP_VERSION.format(name=DOMAIN, version=VERSION, issue_link=ISSUE_URL)
    )


    # Create DATA dict
    hass.data[DOMAIN_DATA] = {}

    # Get "global" configuration.
    username = config_entry.data.get(CONF_USERNAME)
    password = config_entry.data.get(CONF_PASSWORD)
    default_list = config_entry.data.get(CONF_DEFAULT_LIST)

    # Configure the client.
    keep = gkeepapi.Keep()
    try:
        keep.login(username, password)
    except Exception as e:
        _LOGGER.exception(e)
        return False
    await hass.async_add_executor_job(keep.sync)
    all_list = await hass.async_add_executor_job(keep.all)
    for list in all_list:
        if list.title == default_list:
            hass.data[DOMAIN_DATA]["gkeep"] = GkeepData(hass, keep, list)
            break
    else:
        return False
        
    # Add binary_sensor
    #hass.async_add_job(
        #hass.config_entries.async_forward_entry_setup(config_entry, "binary_sensor")
    #)

    # Add sensor
    hass.async_add_job(
        hass.config_entries.async_forward_entry_setup(config_entry, "sensor")
    )


    return True


class GkeepData:
    """This class handle communication and stores the data."""

    def __init__(self, hass, gkeep, list):
        """Initialize the class."""
        self.hass = hass
        self.gkeep = gkeep
        self.list = list

    @Throttle(MIN_TIME_BETWEEN_UPDATES)
    async def update_data(self):
        """Update data."""
        # This is where the main logic to update platform data goes.
        try:
            await self.hass.async_add_executor_job(self.gkeep.sync)
        except Exception as error:  # pylint: disable=broad-except
            _LOGGER.error("Could not sync - %s", error)
        self.hass.data[DOMAIN_DATA]["data"] = self.list


async def check_files(hass):
    """Return bool that indicates if all files are present."""
    # Verify that the user downloaded all files.
    base = f"{hass.config.path()}/custom_components/{DOMAIN}/"
    missing = []
    for file in REQUIRED_FILES:
        fullpath = "{}{}".format(base, file)
        if not os.path.exists(fullpath):
            missing.append(file)

    if missing:
        _LOGGER.critical("The following files are missing: %s", str(missing))
        returnvalue = False
    else:
        returnvalue = True

    return returnvalue


async def async_remove_entry(hass, config_entry):
    """Handle removal of an entry."""
    #try:
        #await hass.config_entries.async_forward_entry_unload(
            #config_entry, "binary_sensor"
        #)
        #_LOGGER.info(
            #"Successfully removed binary_sensor from the blueprint integration"
        #)
    #except ValueError:
        #pass

    try:
        await hass.config_entries.async_forward_entry_unload(config_entry, "sensor")
        _LOGGER.info("Successfully removed sensor from the blueprint integration")
    except ValueError:
        pass

