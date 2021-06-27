#.....Coroutines in Python.........

def searcher():
    import time
    book = "This is a book on Sambhu and Harrry and good"
    time.sleep(5)

    while True:
        text =  (yield )
        if text in book:
            print("Your text is in the book")
        else :
            print("text is not in the book")

search = searcher()
print("Search started...")
next(search)
print("next method run..")
search.send("Sambhu")
input("Press any key:")
search.send("Sambhu and Harrry")

search.close()

search.send("saasa")   #  ye nehin chalegaa
