# Scuffed Virtual Webcam thingy made with Python

## Requirements
- Python 3.9+ https://www.python.org/downloads/
- OBS https://obsproject.com/download

## How to use
1. Download or clone the project
2. Get two images; one for ON state and one for OFF state. Or you can use the default ones
3. run ```main.py --help``` to get a list of available commands
4. Open OBS and set up a virtual webcam, then select it as a camera in Discord/Zoom/Teams or whatever. You can follow [these instructions](https://obsproject.com/forum/resources/obs-virtualcam.539/)

## Commands
```html
-h, --help            show this help message and exit
--list                show a list of all available settings and exit
--save NAME           save settings for easier use by entering a name for a setting (e.g. cat)
--load NAME           load settings by name (e.g. cat)
--on PATH             path to an image that will be shown when the user is talking
--off PATH            path to an image that will be shown when the user is not talking
--volume_threshold INT
                      (OPTIONAL) set the volume threshold. Default: 2000
```
