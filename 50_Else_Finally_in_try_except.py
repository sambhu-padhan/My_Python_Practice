#...Else_Finally_in_try_except.......
f = open("sambhu.txt")
try:
    f1 = open("song.mp3")

except Exception as e :
    print(e)                #  [Errno 2] No such file or directory: 'dd.txt'
else:
    print("Exception is not here.")
finally:
    print("this will be run anyway...")
    f.close()
    f1.close()
