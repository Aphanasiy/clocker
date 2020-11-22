#!/usr/bin/python3


import vlc  # sudo apt-get install vlc && pip3 install python-vlc
import os
import sys
import time


RINGTONES_FOLDER = "ringtones"


def get_sleep_time():
    if (len(sys.argv) < 2):
        print("Time must be specified in first arguement in format [dd[-mm-yy]T]hh:mm")
        sys.exit(1)
    t = sys.argv[1]
    h, m = map(int, t.split(":"))
    lt = time.localtime()
    th, tm, ts = lt.tm_hour, lt.tm_min, lt.tm_sec

    secs_sleep = ((h * 60 + m) * 60 - ((th * 60 + tm) * 60 + ts)) % (24 * 60 * 60)
    return secs_sleep


def choose_track():
    tracks = list(filter(lambda x: x.endswith(".mp3"), os.listdir(RINGTONES_FOLDER)))
    print("Choose track: ")
    for i in range(1, len(tracks) + 1):
        print(f"{i}) {tracks[i - 1]}")
    x = int(input("Your choice: "))
    return os.path.join(RINGTONES_FOLDER, tracks[x - 1])


def alarm(track):
    t = vlc.MediaPlayer(track)
    t.play()
    input("Press Enter to stop")
    t.stop()
    t.release()


stime = get_sleep_time()
track = choose_track()
print("")
print(f"It will be alarmed in {stime // 60} minutes")
time.sleep(stime)
alarm(track)
