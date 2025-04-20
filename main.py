from pynput import keyboard
from sys import argv
import random
from os.path import join 
from os import listdir,system
import pygame

pygame.mixer.init()
arg = argv[-1]
audios = listdir("./audio/")

system('''printf "\033[2A\033[0J"''')
sound_base = ""
if arg in audios:
    sound_base = f"audio/{arg}"
else:
    print("check the sounds in the ./audio dir and run:")
    print("python main.py <audio>")
    exit(1)

press_dir = join(sound_base, "press")
release_dir = join(sound_base, "release")

sounds = {
    "press": {
        "ENTER": pygame.mixer.Sound(join(press_dir, "ENTER.mp3")),
        "SPACE": pygame.mixer.Sound(join(press_dir, "SPACE.mp3")),
        "BACKSPACE": pygame.mixer.Sound(join(press_dir, "BACKSPACE.mp3")),
        "GENERIC": [pygame.mixer.Sound(join(press_dir, f"GENERIC_R{i}.mp3")) for i in range(5)]
    },
    "release": {
        "ENTER": pygame.mixer.Sound(join(release_dir, "ENTER.mp3")),
        "SPACE": pygame.mixer.Sound(join(release_dir, "SPACE.mp3")),
        "BACKSPACE": pygame.mixer.Sound(join(release_dir, "BACKSPACE.mp3")),
        "GENERIC": pygame.mixer.Sound(join(release_dir, "GENERIC.mp3"))
    }
}


def on_press(key):
    try:
        if key == keyboard.Key.enter:
            sounds["press"]["ENTER"].play()
        elif key == keyboard.Key.space:
            sounds["press"]["SPACE"].play()
        elif key == keyboard.Key.backspace:
            sounds["press"]["BACKSPACE"].play()
        else:
            random.choice(sounds["press"]["GENERIC"]).play()
    except Exception as e:
        print("Error:", e)

def on_release(key):
    try:
        if key == keyboard.Key.enter:
            sounds["release"]["ENTER"].play()
        elif key == keyboard.Key.space:
            sounds["release"]["SPACE"].play()
        elif key == keyboard.Key.backspace:
            sounds["release"]["BACKSPACE"].play()
        else:
            sounds["release"]["GENERIC"].play()
    except Exception as e:
        print("Error:", e)
try:
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

except KeyboardInterrupt:
    exit(0)

