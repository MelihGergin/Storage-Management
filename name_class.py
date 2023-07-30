class names():
    a = input("Name             : ")
    b = input("Surname          : ")
    print("Welcome", a, b, "!\n")
    try:
        password = "123456"
        c = input("Enter password   : ")
        if c == password:
            print("The password is correct.\n")
        else:
            print("The password is wrong...\n")
    except:
        print("The password is wrong...")
