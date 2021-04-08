# Scuffed Virtual Webcam thingy made with Python

## Requirements
- Python https://www.python.org/downloads/
- OBS https://obsproject.com/download
- Bunch of Python modules which can be installed via pip

## How to use

1. Download and install Python: https://www.python.org/downloads/ . Test it by opening command prompt (press win + R and type in "cmd") and type in ```py```
2. Download or clone the project
3. Get two images; one for ON state and one for OFF state. Or you can use the shrek and pop cat images (and settings)
4. CD to the project folder
5. run ```main.py --help```for available commands or look at the list below
6. Install pip  by running ```python -m pip install --upgrade pip``` in CMD
7. You probably have to install some Python modules, you can do it by running ```pip install <module name>```. On Windows, when installing PyAudio, you may have to use pipwin instead:
```
pip install pipwin
pipwin install pyaudio
```
8. Open OBS and set up a virtual webcam, then select it as a camera in Discord or whatever. You can follow [these instructions](https://obsproject.com/forum/resources/obs-virtualcam.539/)
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
