# Exersize5...Health management system....
print("\t\t\t\t......HEALTH MANAGEMENT SYSTEM........")

def date():
    import datetime
    return datetime.datetime.now()  # 2021-05-27 16:45:03.295778

dict1 = {1 : "Lock", 2 : "Retrieve"}
dict2 = {1 : "Rajesh", 2 : "Bharat", 3 : "Sarat"}
dict3 = {1 : "Diet", 2 : "Exercise"}
dict4 = {"Rajesh" : "Rajesh_Diet.txt", "Sarat" : "Sarat_Diet.txt", "Bharat" : "Bharat_Diet.txt"}
dict5 = {"Rajesh" : "Rajesh_Exercise.txt", "Sarat" : "Sarat_Exercise.txt", "Bharat" : "Bharat_Exercise.txt"}

# diet_exercise Functon
def diet_exercise_retrive(inp,get_dict2_data) :
 if inp == 1:                                                                                   # for Diet retrieve
  print("Previous diet records of",get_dict2_data,":\n")
  diet_retrieve = dict4.get(get_dict2_data)
  f = open(diet_retrieve,"r")
  reading = f.read()
  print(reading)
  f.close()
 else :                                                                                         # for Exercise retrieve
  print("Previous exercise records of",get_dict2_data,":\n")
  diet_retrieve = dict5.get(get_dict2_data)
  f = open(diet_retrieve, "r")
  reading = f.read()
  print(reading)
  f.close()

def diet_exercise_lock(inp,get_dict2_data) :
 if inp == 1:                                                                                   # for Diet
  print("Enter prefered Diet for",get_dict2_data,":")
  inp = input()
  f = open("Rajesh_Diet.txt","a")
  f.write("\n")
  f.write(str(date()))
  f.write("\t:\t")
  f.write(inp)
  f.close()
  print(inp,"Diet is locked for client -",get_dict2_data,"\t\t.....Thank You...Visit Again...")
 else :                                                                                         # for Exercise
  print("Enter prefered exercise for",get_dict2_data,":")
  inp = input()
  f = open("Rajesh_Exercise.txt", "a")
  f.write("\n")
  f.write(str(date()))
  f.write("\t:\t")
  f.write(inp)
  f.close()
  print(inp, "exercise is locked for client -", get_dict2_data,"\t\t.....Thank You...Visit Again...")


# lock function
def lock_and_retrieve(inp):

  if inp == 1:
    print("select Client to Lock : ")
    print("1.Rajesh\n"
          "2.Bharat\n"
          "3.Sarat\t\t\t\tPress 1 or 2 or 3 :", end=" ")
    inp = int(input())
    get_dict2_data = dict2.get(inp)
    if inp not in dict2 :
     while get_dict2_data not in dict2 :
        print("\t\t\t\t\tPress 1 or 2 or 3 :", end=" ")
        inp = int(input())
        get_dict2_data = dict2.get(inp)
        if inp in dict2 :
            break
        else :
            continue

    print("What to lock for", get_dict2_data," :")
    print("1.Diet\n"
          "2.Exercise\t\t\tPress 1 or 2 : ", end = " ")
    inp = int(input())
    get_dict3_data = dict3.get(inp)
    if get_dict3_data == "Diet":
        print(get_dict3_data)
        diet_exercise_lock(inp,get_dict2_data)
    elif get_dict3_data == "Exercise":
        print(get_dict3_data)
        diet_exercise_lock(inp,get_dict2_data)

    while inp not in dict3:
        print("\t\t\t\t\tPress 1 or 2 : ", end = " ")
        inp = int(input())
        get_dict3_data = dict3.get(inp)
        if get_dict3_data == "Diet":
            print("\t\t\t", get_dict3_data)
            diet_exercise_lock(inp,get_dict2_data)
        elif get_dict3_data == "Exercise":
            print("\t\t\t", get_dict3_data)
            diet_exercise_lock(inp,get_dict2_data)
        else:
            continue
        break

# Retrieve function
  else :
    print("Select Client :")
    print("1.Rajesh\n"
          "2.Bharat\n"
          "3.Sarat\t\t\t\tPress 1 or 2 or 3 :", end=" ")
    inp = int(input())
    get_dict2_data = dict2.get(inp)
    if inp not in dict2:
        while get_dict2_data not in dict2:
            print("\t\t\t\t\tPress 1 or 2 or 3 :", end=" ")
            inp = int(input())
            get_dict2_data = dict2.get(inp)
            if inp in dict2:
                break
            else:
                continue
    print("What to retrieve of client", get_dict2_data," :")
    print("1.Diet\n"
          "2.Exercise\t\t\tPress 1 or 2 : ", end = " ")
    inp = int(input())
    get_dict3_data = dict3.get(inp)
    if get_dict3_data == "Diet":
        print(get_dict3_data)
        diet_exercise_retrive(inp,get_dict2_data)
    elif get_dict3_data == "Exercise":
        print(get_dict3_data)
        diet_exercise_retrive(inp, get_dict2_data)

    while inp not in dict3:
        print("\t\t\t\t\tPress 1 or 2 : ", end=" ")
        inp = int(input())
        get_dict3_data = dict3.get(inp)
        if get_dict3_data == "Diet":
            print("\t\t\t", get_dict3_data)
            diet_exercise_retrive(inp, get_dict2_data)
        elif get_dict3_data == "Exercise":
            print("\t\t\t", get_dict3_data)
            diet_exercise_retrive(inp, get_dict2_data)
        else:
            continue
        break



# main Module
print("1.Lock\n"
      "2.Retrieve\t\t\tPress 1 or 2 : ", end = "")
inp  = int(input())
get_dict1_data = dict1.get(inp)

if get_dict1_data == "Lock" :
      print("\t\t\t",get_dict1_data)
      lock_and_retrieve(inp)
elif get_dict1_data == "Retrieve" :
      print("\t\t\t",get_dict1_data)
      lock_and_retrieve(inp)
while inp not in dict1 :
    print("\t\t\t\t\tPress 1 or 2 :", end = " ")
    inp = int(input())
    get_dict1_data = dict1.get(inp)
    if get_dict1_data == "Lock":
        print("\t\t\t",get_dict1_data)
        lock_and_retrieve(inp)
    elif get_dict1_data == "Retrieve":
        print("\t\t\t",get_dict1_data)
        lock_and_retrieve(inp)
    else :
        continue
    break



""" OUTPUT

				......HEALTH MANAGEMENT SYSTEM........
1.Lock
2.Retrieve			Press 1 or 2 : 2
			 Retrieve
Select Client :
1.Rajesh
2.Bharat
3.Sarat				Press 1 or 2 or 3 : 2
What to retrieve of client Bharat  :
1.Diet
2.Exercise			Press 1 or 2 :  2
Exercise
Previous exercise records of Bharat :

2021-05-28 22:58:06.957761	:	Push-ups
2021-05-28 23:01:43.080540	:	saolin
2021-05-28 23:19:00.778763	:	Armring
2021-05-29 09:13:00.877714	:	aassasdffggfg
2021-05-29 09:14:56.239917	:	ddsrrr
2021-05-29 09:17:14.128559	:	dddasa dgf
2021-05-29 09:17:46.280216	:	fdfdfd fdggf
2021-05-29 09:24:07.576085	:	sdsdsd
2021-05-29 09:27:31.047243	:	assa
"""