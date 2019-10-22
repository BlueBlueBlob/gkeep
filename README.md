[![CodeFactor](https://www.codefactor.io/repository/github/blueblueblob/gkeep/badge)](https://www.codefactor.io/repository/github/blueblueblob/gkeep)




## Installation

1. Using the tool of choice open the directory (folder) for your HA configuration (where you find `configuration.yaml`).
2. If you do not have a `custom_components` directory (folder) there, you need to create it.
3. In the `custom_components` directory (folder) create a new folder called `gkeep`.
4. Download _all_ the files from the `custom_components/gkeep/` directory (folder) in this repository.
5. Place the files you downloaded in the new directory (folder) you created.
6. Restart Home Assistant
7. Choose:
   - Add `gkeep:` to your HA configuration.
   - In the HA UI go to "Configuration" -> "Integrations" click "+" and search for "Google Keep"

Using your HA configuration directory (folder) as a starting point you should now also have this:

```text
custom_components/gkeep/.translations/en.json
custom_components/gkeep/__init__.py
custom_components/gkeep/config_flow.py
custom_components/gkeep/const.py
custom_components/gkeep/manifest.json
custom_components/gkeep/sensor.py
```

## Notes
You need an app password if you have 2AF enable