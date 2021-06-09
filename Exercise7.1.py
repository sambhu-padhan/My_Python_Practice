# ----Alarm timing----
# Take_water = in every 1 minute
# take_Body_Ex exrcise = in every 2 minutes
# You can change the timing

import Exercise7
import time
import datetime
dateandtime = datetime.datetime.now()
local_time = time.asctime(time.localtime(time.time()))
# from threading import Timer

print("\n\t\t\t\t.....Health Program For You.....\n")
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

   ExecutionTime1 = Exercise7.takeWater()
   timeleft1 = BodyExerciseTiming-(TakeWaterTiming+ExecutionTime1)

   if timeleft1<0 :
      print("You are not focusing on alarm,time exceed.")
      print("You are not caring of your Health, Please follow the Health Proghram")
      timeleft1 = 0

   print("Time Left for next task : ", timeleft1," seconds\n")
   time.sleep(timeleft1)

   ExecutionTime2 = Exercise7.bodyExercise()
   timeleft2 = TakeWaterTiming-(ExecutionTime2)

   if timeleft2<0 :
      print("You are not focusing on alarm,time exceed.")
      print("You are not caring of your Health, Please follow the Health Proghram")
      timeleft2 = 0

   print("Time Left for next task : ", timeleft2," seconds\n")
   time.sleep(timeleft2)

   ExecutionTime3 = Exercise7.takeWater()
   temp = ExecutionTime3
