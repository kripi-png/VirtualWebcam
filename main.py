import PySimpleGUI as sg
import audioop
import pyaudio
import argparse
import json
import os

TIMEOUT = 10 # ms
RATE = 16000
FORMAT = pyaudio.paInt16
CHANNELS = 1
CHUNK = 1024
RECORD_SECONDS = .5

def isFile(name): return os.path.exists(name)
def is_speech(stream, VOLUME_TRESHOLD):
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        rms = audioop.rms(data, 2)
        return True if rms > VOLUME_TRESHOLD else False

def saveSettings(save, ON, OFF, VOLUME_TRESHOLD):
    """saves given attributes into a json file for later use"""
    with open("./settings/" + save+".json", "w") as f:
        json.dump({"on": ON, "off": OFF, "vol": VOLUME_TRESHOLD}, f)
        print("Settings saved")

def loadSettings(save):
    """load ON, OFF and VOLUME_THRESHOLD settings from a file"""
    try:
        with open("./settings/" + save+".json", "r") as f:
            data = json.load(f)
            print("Loaded settings")
            return data["off"], data["on"], data["vol"]
    except Exception as e:
        raise OSError("Invalid setting name: " + save)

def listSettings():
    files = os.listdir("./settings")
    print("List of available settings:\n" + "\n".join(["- "+ x[:-5] for x in files]))

def main(args):
    if not os.path.isdir("./settings"): os.mkdir("settings") # create settings folder if it does not exist
    if args.list: return listSettings() # show a list of saved settings and exit
    if not args.load and (not args.on or not args.off): raise OSError("You must enter valid image paths using --on and --off")

    if args.load:
        OFF, ON, VOLUME_TRESHOLD = loadSettings(args.load)
    else:
        OFF= args.off
        ON = args.on
        VOLUME_TRESHOLD = args.volume_threshold

    if not args.on or not args.off: # if user is trying to save with no settings
        if args.save:
            raise Exception("Trying to save with no paths given.")

    if not isFile(OFF): raise OSError(f"Invalid image path: '{OFF}' Please make sure given paths are valid.")
    if not isFile(ON): raise OSError(f"Invalid image path: '{ON}' Please make sure given paths are valid.")

    if args.save: saveSettings(args.save, ON, OFF, VOLUME_TRESHOLD)

    print("Current settings:")
    print("ON - " + ON)
    print("OFF - " + OFF)
    print("VOLUME_TRESHOLD - " + str(VOLUME_TRESHOLD))

    sg.theme('DarkAmber')
    LAYOUT = [  [sg.Image(filename=OFF, key="IMAGE")] ]
    WINDOW = sg.Window('VirtualWebcam_Python', LAYOUT, margins=(0,0), element_padding=(0,0))

    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    while True:
        event, values = WINDOW.read(timeout=TIMEOUT)
        if event == sg.WIN_CLOSED or event == 'Cancel': break

        newState = ON if is_speech(stream, VOLUME_TRESHOLD) else OFF
        if WINDOW["IMAGE"].Filename != newState:
            WINDOW["IMAGE"].update(newState)
            WINDOW["IMAGE"].Filename = newState

    WINDOW.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Creates a window with an image for OBS to use as a source for a virtual webcam")

    parser.add_argument("--list", help="show a list of all available settings and exit", action="store_true")
    parser.add_argument("--save", help="save settings for easier use by entering a name for a setting (e.g. cat)")
    parser.add_argument("--load", help="load settings by name (e.g. cat)")
    parser.add_argument("--on", help="path to an image that will be shown when the user is talking")
    parser.add_argument("--off", help="path to an image that will be shown when the user is not talking")
    parser.add_argument("--volume_threshold", help="(OPTIONAL) set the volume threshold. Default: 2000", type=int, default=2000)

    args = parser.parse_args()
    main(args)
