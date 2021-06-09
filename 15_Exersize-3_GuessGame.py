n = 17
# Write a program for a game where you print like
#  Number of Guesses..
#  Number of Guesses left..
#  Number of Guesses he took to finish..
#  Game over..

print("\t\t...Game start....")
print("Total number of Guesses\t\t   : 7")
guesses = 7
print("Guess a Number between 1 to 50 : ", end = "")
x = int(input())

while(guesses >= 1) :

   if x == 17 :
      print("\t\t\t\t\t\t\t\t\tYou won it... Got-$50\n"
          "\t\t\t\t\t\t\t\t\tGame Over..Thank you")
      break

   elif 0<=x<=10 :
      print("\t\t\t\t\t\t\t\t\t",x,"is too smaller than the actual Number..")

   elif 11 <= x<=16:
      print("\t\t\t\t\t\t\t\t\t",x,"is smaller than the actual one, but"
                            " You are too close to end the game.")

   elif 26 <= x <= 50:
       print("\t\t\t\t\t\t\t\t\t", x, "is greater than the actual number.")

   elif 18 <= x <=25:
      print("\t\t\t\t\t\t\t\t\t" ,x, "is greater than the actual one, but"
                                   " You are too close to end the game.")

   elif x >= 50 :
       print("\t\t\t\t\t\t\tChoose number between 1 to 50..")

   guesses = guesses - 1
   print("Number of guesses left :", guesses)
   if 1<=guesses<=6 :
     print("Guess a Number between 1 to 50 :", end = " ")
     x = int(input())
     continue
   else:
       print("\t\t\t\t\t\t\t\tGame Over..You Lost..")


"""  OUTPUT
		...Game start....
Total number of Guesses		   : 7
Guess a Number between 1 to 50 : 45
									 45 is greater than the actual number.
Number of guesses left : 6
Guess a Number between 1 to 50 : 1
									 1 is too smaller than the actual Number..
Number of guesses left : 5
Guess a Number between 1 to 50 : 30
									 30 is greater than the actual number.
Number of guesses left : 4
Guess a Number between 1 to 50 : 20
									 20 is greater than the actual one, but You are too close to end the game.
Number of guesses left : 3
Guess a Number between 1 to 50 : 15
									 15 is smaller than the actual one, but You are too close to end the game.
Number of guesses left : 2
Guess a Number between 1 to 50 : 18
									 18 is greater than the actual one, but You are too close to end the game.
Number of guesses left : 1
Guess a Number between 1 to 50 : 17
									You won it... Got-$50
									Game Over..Thank you
"""
