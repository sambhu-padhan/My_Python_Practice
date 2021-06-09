# Make a game ( SNAKE-WATER-GUN)
# 10 -LEVELS
# USING RANDOM MODULE
import random

dict1 = {"S" : "SNAKE", "W" : "WATER", "G" : "GUN"}
list1 = ["SNAKE","WATER","GUN"]
print("\t\t\t....SNAKE-WATER-GUN.....")

global y
y=0

def points() :
    global y
    y =int(y)+1

def fun10levels(level) :

 print("Choose S or W or G : ", end = " ")
 inp = input()
 x = inp.capitalize()
 if x in dict1:
    print("\t\tYou picked :", dict1.get(x), end=" ")
 while x not in dict1 :
    print("\t\t\t\t\t\t\tInvalid input")
    print("Choose S or W or G : ", end=" ")
    inp = input()
    x = inp.capitalize()
    if x in dict1 :
        print("\t\tYou picked :", dict1.get(x), end=" ")
        break
    else :
        continue

# rand = random.choice(list1)
# print(rand)
 rand = random.choice(list1)
 print("\t\tOponent picked :",rand)
 if dict1.get(x) == rand :
    print("You won 1-Point.")
    print("(Level", level, "completed)""\n")
    points()
 else :
    print("You lost, you got",0,"point")
    print("(Level",level,"completed)""\n")


n = 10
level = 1
lifeleft = 10
for i in range (n):
    print("LEVEL : ", level, "\t\t\t\t\t\t\t\tYOUR LIFELINE LEFT : ", lifeleft)
    print("\t\t[SNAKE-WATER-GUN]")
    fun10levels(level)
    lifeleft = 10 - level
    level = level + 1

print("\t\t\t\t\tYou won total points : ",y)
print("\t\t\t\t\tGAME OVER...THANK YOU...")



"""OUTPUT
				....SNAKE-WATER-GUN.....
LEVEL :  1 								YOUR LIFELINE LEFT :  10
		[SNAKE-WATER-GUN]
Choose S or W or G :  s
		You picked : SNAKE 		Oponent picked : SNAKE
You won 1-Point.
(Level 1 completed)

LEVEL :  2 								YOUR LIFELINE LEFT :  9
		[SNAKE-WATER-GUN]
Choose S or W or G :  w
		You picked : WATER 		Oponent picked : WATER
You won 1-Point.
(Level 2 completed)

LEVEL :  3 								YOUR LIFELINE LEFT :  8
		[SNAKE-WATER-GUN]
Choose S or W or G :  s
		You picked : SNAKE 		Oponent picked : SNAKE
You won 1-Point.
(Level 3 completed)

LEVEL :  4 								YOUR LIFELINE LEFT :  7
		[SNAKE-WATER-GUN]
Choose S or W or G :  s
		You picked : SNAKE 		Oponent picked : WATER
You lost, you got 0 point
(Level 4 completed)

LEVEL :  5 								YOUR LIFELINE LEFT :  6
		[SNAKE-WATER-GUN]
Choose S or W or G :  g
		You picked : GUN 		Oponent picked : SNAKE
You lost, you got 0 point
(Level 5 completed)

LEVEL :  6 								YOUR LIFELINE LEFT :  5
		[SNAKE-WATER-GUN]
Choose S or W or G :  g
		You picked : GUN 		Oponent picked : SNAKE
You lost, you got 0 point
(Level 6 completed)

LEVEL :  7 								YOUR LIFELINE LEFT :  4
		[SNAKE-WATER-GUN]
Choose S or W or G :  g
		You picked : GUN 		Oponent picked : GUN
You won 1-Point.
(Level 7 completed)

LEVEL :  8 								YOUR LIFELINE LEFT :  3
		[SNAKE-WATER-GUN]
Choose S or W or G :  g
		You picked : GUN 		Oponent picked : GUN
You won 1-Point.
(Level 8 completed)

LEVEL :  9 								YOUR LIFELINE LEFT :  2
		[SNAKE-WATER-GUN]
Choose S or W or G :  s
		You picked : SNAKE 		Oponent picked : GUN
You lost, you got 0 point
(Level 9 completed)

LEVEL :  10 								YOUR LIFELINE LEFT :  1
		[SNAKE-WATER-GUN]
Choose S or W or G :  w
		You picked : WATER 		Oponent picked : SNAKE
You lost, you got 0 point
(Level 10 completed)

					You won total points :  5
					GAME OVER...THANK YOU...

"""