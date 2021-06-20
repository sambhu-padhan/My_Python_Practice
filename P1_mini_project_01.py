
# ......Library management system..............

class Library :
    def __init__(self,getlist,getDict):
        self.getlist = getDict
        self.getDict = getDict


    def DisplayBook(getlist):
        x=0
        for index,item in enumerate(getlist) :
            print(f"{index+1} : {getlist[x]}")
            x+=1

    def LendBook(getlist,getDict):
        print("Enter Book Name : ", end=" ")
        inp = input()
        inp = inp.upper()
        if inp == "Q" :
            return
        if inp in getDict :
            print(f"You can't Lend {inp} book, ")
            print(f"{inp} book is taken by {getDict.get(inp)}")
        elif inp in getlist :
            print(inp)
            print("Enter Your name :",end=" ")
            inpt = input()
            getDict.update({inp:inpt})
            print(f"You Got {inp} book.")
            print("\t\t\t\tThank you..Visit again...")
        else :
            print("This book is not present in the Library.")

    def AddBook(getlist):
        print("Enter Book Name : ",end=" ")
        inp = input()
        inp = inp.upper()
        if inp == "Q" :
            return
        if inp in getlist :
            print("This book is already present in Library.")
            Library.AddBook(getlist)
        else :
            getlist.append(inp)
            print(f"{inp} Book is added to the Library.")

    def ReturnBook(getlist,getDict):
        inp = input()
        inp = inp.upper()
        if inp == "Q" :
            return
        if inp not in getlist :
            print("Please Enter valid Book name :",end=" ")
            Library.ReturnBook(getlist,getDict)
        elif inp in getDict :
            getDict.pop(inp)
            print("You have securely returned the book.")
            print("\t\t\t\tThank you..Visit Again..")
        else :
            print("Please enter valid book name : ",end=" ")
            Library.ReturnBook(getDict,getlist)

    def DeleteBook(getList,getDict):
        inp = input()
        inp = inp.upper()
        if inp == "Q" :
            return
        if inp in getList :
            if inp not in getDict :
                getList.remove(inp)
                print(getDict)
                print(f"{inp} book is successfully deleted ..\n \t\t\t\tThank you..Visit Again..")
            else :
                print("You cann't delete this book,")
                print(f"This book is taken by {getDict.get(inp)}")
        else :
            print("Please enter valid book name : ",end = " ")
            Library.DeleteBook(getList,getDict)



def main() :
    dict = {"PYTHON": "MAITRY", "JAVA": "SAMBHU", "CPP": "DEV", "DBMS": "CHAUDHARY"}
    list = ["PYTHON", "JAVA", "CPP", "DBMS", "OS", "C"]
    print("\t\t\t............WELCOME TO MY LIBRARY........\n")

    Sambhu = Library(list, dict)

    print("Display Books [ Enter D]\tLend Book[ Enter L ]\tReturn a Book[ Enter R ]\tAdd a Book[ Enter A ]\tDelete Book[ Enter DEL ]\tExit[ Enter Q ]")
    print("Plaese Enter : ",end=" ")

    while (True) :
     inp = input()
     inp  = inp.upper()
     if inp == "D" :
        print("Books are available : \n")
        Library.DisplayBook(list)
        print("Display Books [ Enter D]\tLend Book[ Enter L ]\tReturn a Book[ Enter R ]\tAdd a Book[ Enter A ]\tDelete Book[ Enter DEL ]\tExit[ Enter Q ]")
        print("Plaese Enter : ", end=" ")
     elif inp == "L":
        print("@@ Lend Book @@")
        Library.LendBook(list,dict)
        print("Display Books [ Enter D]\tLend Book[ Enter L ]\tReturn a Book[ Enter R ]\tAdd a Book[ Enter A ]\tDelete Book[ Enter DEL ]\tExit[ Enter Q ]")
        print("Plaese Enter : ", end=" ")
     elif inp == "A" :
        print(" @ Add Book @")
        Library.AddBook(list)
        print("Display Books [ Enter D]\tLend Book[ Enter L ]\tReturn a Book[ Enter R ]\tAdd a Book[ Enter A ]\tDelete Book[ Enter DEL ]\tExit[ Enter Q ]")
        print("Plaese Enter : ", end=" ")
     elif inp == "R":
        print("@ Return Book @")
        print("Enter Book name : ", end=" ")
        Library.ReturnBook(list,dict)
        print("Display Books [ Enter D]\tLend Book[ Enter L ]\tReturn a Book[ Enter R ]\tAdd a Book[ Enter A ]\tDelete Book[ Enter DEL ]\tExit[ Enter Q ]")
        print("Plaese Enter : ", end=" ")
     elif inp == "DEL" :
        print("@ Delete Book @")
        print("Enter book name :", end=" ")
        Library.DeleteBook(list,dict)
        print("Display Books [ Enter D]\tLend Book[ Enter L ]\tReturn a Book[ Enter R ]\tAdd a Book[ Enter A ]\tDelete Book[ Enter DEL ]\tExit[ Enter Q ]")
        print("Plaese Enter : ", end=" ")
     elif inp == "Q" :
        print("Display Books [ Enter D]\tLend Book[ Enter L ]\tReturn a Book[ Enter R ]\tAdd a Book[ Enter A ]\tDelete Book[ Enter DEL ]\tExit[ Enter Q ]")
        print("Plaese Enter : ",end=" ")
     else :
        print("Please Enter Valid KeyWord :",end=" ")


if __name__ == '__main__':
    main()