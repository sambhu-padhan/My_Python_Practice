# ----Alarm timing----

# Take_water and eye Exer. = in every 1 minute  (you can change it)
# take_Body_Ex exrcise     = in every 2 minutes (you can change it)
# You can change the timing
# I have used a common song for alarm

import time
import datetime
dateandtime = datetime.datetime.now()
from pygame import mixer
mixer.init()
mixer.music.load("song.mp3")
mixer.music.set_volume(0.7)


def takeWater() :
    mixer.music.play()
    start = int(time.time())
    local_time = time.asctime(time.localtime(time.time()))
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
    local_time = time.asctime(time.localtime(time.time()))
    print(f"plelase complete your Body Exercise  \t\t\t\t\t\t{local_time}")
    print("Please press any key for confirmation :",end = " ")
    inp = input()
    if inp :
        mixer.music.stop()
        print("OK, Thank you..keep it up...\n")
    end = int(time.time())
    ExecutionTime2 = end-start
    return ExecutionTime2

#........................My program start here.............................#

print("\n\t\t\t\t.....Health Program For You.....\n")
local_time = time.asctime(time.localtime(time.time()))
print(local_time)

BodyExerciseTiming = 120    # fix your (take_Body_Ex exrcise) timting here in seconds
TakeWaterTiming    =  60    # fix your (take_Water) timting here in seconds
temp = 0

for i in range(2) :                     # Change according to your Health program limit
   timeleft = TakeWaterTiming-temp
   if timeleft<0 :
      print("You are not focusing on alarm,time exceed.")
      print("You are not caring of your Health, Please follow the Health Proghram")
      timeleft = 0

   print("Time Left for next task : ", timeleft," seconds\n")
   time.sleep(timeleft)

   ExecutionTime1 = takeWater()
   timeleft1 = BodyExerciseTiming-(TakeWaterTiming+ExecutionTime1)

   if timeleft1<0 :
      print("You are not focusing on alarm,time exceed.")
      print("You are not caring of your Health, Please follow the Health Proghram")
      timeleft1 = 0

   print("Time Left for next task : ", timeleft1," seconds\n")
   time.sleep(timeleft1)

   ExecutionTime2 = bodyExercise()
   timeleft2 = TakeWaterTiming-(ExecutionTime2)

   if timeleft2<0 :
      print("You are not focusing on alarm,time exceed.")
      print("You are not caring of your Health, Please follow the Health Proghram")
      timeleft2 = 0

   print("Time Left for next task : ", timeleft2," seconds\n")
   time.sleep(timeleft2)

   ExecutionTime3 = takeWater()
   temp = ExecutionTime3
