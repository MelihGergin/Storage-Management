class storage():
    try:
        print("Materials and Quantities in the Storage"
            "\n\n1- M4 bolts \n2- M6 bolts \n3- 0.4mm 1000x2000mm2 304 stainless steel sheet")
        a = input("Please select a material (1/2/3): ")
        list = ['1- Quantity of M4 bolts: ', 300, '2- Quantity of M6 bolts: ', 300, '3- 0.4mm 1000x2000mm2 Quantity of 304 stainless steel sheet: ', 20]
        if a == "1":
            print(list)
            b = input("\nWould you like to change the quantity of first material? (Yes/No) ")
            if b == "Yes":
                c = int(input("Enter new data: "))
                list[1] = c
                print("\nNew list: ")
                print(list)
            else:
                print("Program terminated...")
        elif a == "2":
            print(list)
            d = input("\nWould you like to change the quantity of second material? (Yes/No) ")
            if d == "Yes":
                e = int(input("Enter new data: "))
                list[3] = e
                print("\nNew list: ")
                print(list)
            else:
                print("Program terminated...")
        elif a == "3":
            print(list)
            f = input("\nWould you like to change the quantity of third material? (Yes/No) ")
            if f == "Yes":
                g = int(input("Enter new data: "))
                list[5] = g
                print("\nNew list: ")
                print(list)
            else:
                print("Program terminated...")
        else:
            print("Program terminated...")
    except:
        print("Error...")
