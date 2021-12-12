import json
import os.path
import sys
import time
import random

# created using - https://patorjk.com/software/taag/#p=display&f=Graffiti&t=NoiseBox
BANNER = r"""
 _______         .__             __________              
 \      \   ____ |__| ______ ____\______   \ _______  ___
 /   |   \ /  _ \|  |/  ___// __ \|    |  _//  _ \  \/  /
/    |    (  <_> )  |\___ \\  ___/|    |   (  <_> >    < 
\____|__  /\____/|__/____  >\___  >______  /\____/__/\_ \
        \/               \/     \/       \/            \/
NoiseBox - Background noise generator for concentration in your terminal. 
"""
print(BANNER)
from pygame import mixer  # noqa

DEBUG = False  # Change this to `True` to print what's played

if getattr(sys, 'frozen', False):
    APP_PATH = os.path.abspath(os.path.dirname(sys.executable))
else:
    APP_PATH = os.path.dirname(os.path.abspath(__file__))

SOUNDS = {}
with open(os.path.join(APP_PATH, "mix.json")) as j:
    MIX = json.load(j)

MIX_BANNER = MIX["banner"]
MIX_DESCRIPTION = MIX["description"]

SECONDS_MIN = MIX["random_pick_seconds_min"]
SECONDS_MAX = MIX["random_pick_seconds_max"]
START_ON = MIX["random_pick_start_on_seconds"]
CHANNELS = MIX["channels"]
RANDOM_SOUNDS = MIX["randomly_pick_and_play"]


def play(item, loops):
    track = item["sound"]
    volume = item["vol"]
    if DEBUG:
        if loops == -1:
            print("Looping '{0}' at volume {1}".format(track, volume))
        else:
            print("Play '{0}' at volume {1}".format(track, volume))
    SOUNDS[track].set_volume(volume)
    SOUNDS[track].play(loops)


def main():
    print("=" * 20)
    print("Mix - ", MIX_DESCRIPTION)
    print(MIX_BANNER)
    print("=" * 20)
    if DEBUG:
        print("----")
    mixer.init()
    mixer.set_num_channels(CHANNELS)
    for k, value in MIX["sounds"].items():
        SOUNDS[k] = mixer.Sound(os.path.join(APP_PATH, "noise", value))
    for track in MIX["loop"]:
        play(track, loops=-1)
    do_random_pick()


def do_random_pick():
    time.sleep(START_ON)
    play_random_pick()
    while True:
        next_play = random.randrange(SECONDS_MIN, SECONDS_MAX)
        time.sleep(next_play)
        play_random_pick()


def play_random_pick():
    if not RANDOM_SOUNDS:
        return
    track = random.choice(RANDOM_SOUNDS)
    play(track, loops=0)


if __name__ == "__main__":
    main()
