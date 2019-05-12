# excersise , diet 


# excersise :- seated solder plus, cable crossover ,pushup

# lock or retrive function
def getdate():
    import datetime
    return datetime.datetime.now()


def rohan_lock():
    print("press1: excersise lock ")
    print("press2: diet lock ")
    sel = int(input());
    if sel == 1:
        print("enter which excersise you do :- ")
        ex = input();
        rl = open("rohan excersise.txt" , "a")
        ex = str(getdate()) + " " + ex + "\n"
        rl.write(ex)
        print("adding successfully :) ")
        rl.close()
    elif sel == 2:
        print("enter which you eat : ")
        ex = input()
        rl = open("rohan diet.txt" , "a")
        ex = str(getdate()) + " " + ex + "\n"
        rl.write(ex)
        print("adding successfully :) ")
        rl.close()
    else:
        print("invalid choice ")
def harry_lock():
    print("press1: excersise lock ")
    print("press2: diet lock ")
    sel = int(input());
    if sel == 1:
        print("enter which excersise you do :- ")
        ex = input();
        hl = open("harry excersise.txt" , "a")
        ex = str(getdate()) + " " + ex + "\n"
        hl.write(ex)
        print("adding successfully :) ")
        hl.close()
    elif sel == 2:
        print("enter which you eat : ")
        ex = input()
        hl = open("harry diet.txt" , "a")
        ex = str(getdate()) + " " + ex + "\n"
        hl.write(ex)
        print("adding successfully :) ")
        hl.close()
    else:
        print("invalid choice ")
def hemmad_lock():
    print("press1: excersise lock ")
    print("press2: diet lock ")
    sel = int(input());
    if sel == 1:
        print("enter which excersise you do :- ")
        ex = input();
        ml = open("hemmad excersise.txt" , "a")
        ex = str(getdate()) + " " + ex + "\n"
        ml.write(ex)
        print("adding successfully :) ")
        ml.close()
    elif sel == 2:
        print("enter which you eat : ")
        ex = input()
        ml = open("hemmad diet.txt" , "a")
        ex = str(getdate()) + " " + ex + "\n"
        ml.write(ex)
        print("adding successfully :) ")
        ml.close()
    else:
        print("invalid choice ")



def rohan_retrive():
    print(" press 1:- excersise retrive ")
    print(" press 2:- dite retrive ")
    sel = int(input())
    if sel == 1:
        rr = open("rohan excersise.txt")
        for line in rr:
            print(line , end = "");
        rr.close();
    elif sel == 2:
        rr = open("rohan diet.txt")
        for line in rr:
            print(line , end = "");
        rr.close();
    else:
        print("invalid choice ")

def harry_retrive():
    print(" press 1:- excersise retrive ")
    print(" press 2:- dite retrive ")
    sel = int(input())
    if sel == 1:
        rr = open("harry excersise.txt")
        for line in rr:
            print(line , end = "");
        rr.close();
    elif sel == 2:
        rr = open("harry diet.txt")
        for line in rr:
            print(line , end = "");
        rr.close();
    else:
        print("invalid choice ")

def hemmad_retrive():
    print(" press 1:- excersise retrive ")
    print(" press 2:- dite retrive ")
    sel = int(input())
    if sel == 1:
        rr = open("hemmad excersise.txt")
        for line in rr:
            print(line , end = "");
        rr.close();
    elif sel == 2:
        rr = open("hemmad diet.txt")
        for line in rr:
            print(line , end = "");
        rr.close();
    else:
        print("invalid choice ")








print("press 1: lock ")

print("press 2: retrive ")

select = int(input())

if select == 1:
    print("press 1: rohan ")
    print("press 2: harry ")
    print("press 3: hemmad ")
    name = int(input())
    if name == 1:
        rohan_lock()
    elif name == 2:
        harry_lock()
    elif name == 3:
        hemmad_lock()
    else:
        print("invalid choice ")
elif select == 2:
    print("press 1: rohan ")
    print("press 2: harry ")
    print("press 3: hemmad ")
    name = int(input())
    if name == 1:
        rohan_retrive()
    elif name == 2:
        harry_retrive()
    elif name == 3:
        hemmad_retrive()
    else:
        print("invalid choice ")
else:
    print("enter valid choice ")


