# Create a Dictionary and take input from
# the user and return the meaning of the word from the dictionary......


di = {"Sambhu":"Sambhu is a Legendary person in the world.\n"
               "He will become the next indian idol of 2021.\n"
               "you can contact him through contact number--9348867149....",
      "Ankit":"Egg",
      "Rame":"Alu",
      "Bilasini":"Achar",
      "Seema" : {"s":"Achar","B":"MAngo","D":"Tomato","R":"Fruits"}}
print("Enter word : ")
inpnum = input()

# print(di[inpnum])

if (inpnum in di):
    {
      print(di[inpnum])
    }
else:
    {
        print("Sorry, Word is not in the Dictionary or\n"
              "You are entering invalid word.\n"
              "Thank you..")
    }
