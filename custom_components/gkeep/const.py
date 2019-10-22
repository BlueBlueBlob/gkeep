"""Constants for gkeep."""
# Base component constants
DOMAIN = "gkeep"
DOMAIN_DATA = f"{DOMAIN}_data"
VERSION = "0.0.2"
PLATFORMS = ["sensor"]
REQUIRED_FILES = [
    ".translations/en.json",
    "binary_sensor.py",
    "const.py",
    "config_flow.py",
    "manifest.json",
    "sensor.py",
    "services.yaml",
]
ISSUE_URL = "https://github.com/BlueBlueBlob/gkeep/issues"
ATTRIBUTION = "Data from this is provided by gkeep."

# Icons
ICON = "mdi:format-list-checkbox"

# Device classes


# Configuration
CONF_USERNAME = "username"
CONF_PASSWORD = "password"
CONF_DEFAULT_LIST = "default_list"

# Defaults
DEFAULT_NAME = DOMAIN

#Services attributes
ATTR_ITEM_TITLE = "item_title"
ATTR_ITEM_CHECKED = "item_checked"

#Services names
SERVICE_NEW_ITEM = "new_item"
SERVICE_ITEM_CHECKED = "item_checked"
