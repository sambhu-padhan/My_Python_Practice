import time
import datetime
dateandtime = datetime.datetime.now()
local_time = time.asctime(time.localtime(time.time()))
from threading import Timer

from pygame import mixer
mixer.init()
mixer.music.load("song.mp3")
mixer.music.set_volume(0.7)

def takeWater() :
    mixer.music.play()
    start = int(time.time())
    print("please take few minutes of eye Exercise and")
    print(f"plelase take 250 ml of water \t\t\t\t\t\t{local_time}")
    print("Please press any key for confirmation :",end = " ")
    toc = int(time.time())
    inp = input()
    if inp :
        mixer.music.stop()
        print("OK, Thank you..keep it up...\n")
    end = int(time.time())
    executiontime1 = end-start
    return executiontime1

def bodyExercise() :
    mixer.music.play()
    start = int(time.time())
    print(f"plelase complete your Exercise  \t\t\t\t\t\t{local_time}")
    print("Please press any key for confirmation :",end = " ")
    inp = input()
    if inp :
        mixer.music.stop()
        print("OK, Thank you..keep it up...\n")
    end = int(time.time())
    ExecutionTime2 = end-start
    return ExecutionTime2

