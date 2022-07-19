from quick_sqlite import Database

def menu():
    choice = input("=MENU=\n1)register\n2)login:")
    if choice == "1":
        register()

    elif choice == "2":
        login()

#you can detele it cuz it is just for me to check the data
    elif choice == "3":
        checkdata()

    elif choice == "4":
        deteledata()
#=========================================================
    else:
        menu()

def register():
    data = Database("userdata.db")
    name = input("create a name:")
    pw = input("create a password:")
    check = data.get(name)
    if check == False:
        data.set(name, pw)
        print("successful to register!")
        home()
    else:
        print("!ERROR! create another name!")
        menu()


def login():
    data = Database("userdata.db")
    name = input("name:")
    pw = input("password:")
    checkname = data.get(name)
    if checkname != None:
        checkpw = data.get(name)
        if pw == checkpw:
            print("successful to login!")
            home()
        else:
            print("!ERROR! username or password is wrong!")
            menu()
    else:
        print("!ERROR! username or password is wrong!")
        menu()
    
def home():
    #do something after user register/login
    print("this is home")


#you can detele it cuz it is just for me to check the data
def checkdata():
    data = Database("userdata.db")
    a = data.get_all()
    print(a)
    menu()

def deteledata():
    data = Database("userdata.db")
    detele = input("which userdata do u want to detele(type his name)")
    data.delete(detele)
    print(f"deteled userdata:{detele}")
    menu()
#=========================================================