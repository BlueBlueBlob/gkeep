"""Constants for gkeep."""
# Base component constants
DOMAIN = "gkeep"
DOMAIN_DATA = f"{DOMAIN}_data"
VERSION = "0.0.1"
PLATFORMS = ["sensor"]
REQUIRED_FILES = [
    ".translations/en.json",
    "binary_sensor.py",
    "const.py",
    "config_flow.py",
    "manifest.json",
    "sensor.py",
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
