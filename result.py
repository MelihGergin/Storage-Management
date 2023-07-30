import name_class
name = name_class.names()
try:
    if name.c == name.password:
        import storage_class
        storage1 = storage_class.storage()
        print("\nNew list: ", storage1.list)
        print("\nGenerating .txt output of new data...")
        dosya = open(r"C:\Users\Melih\Desktop\Storage_New_Data_Output.txt", mode="w")
        dosya.write("///////////////////////////////////////////////////////////////////////////////\n")
        dosya.write("\nGenerating .txt output of new data...\n\n")
        dosya.write("1- Quantity of M4 bolts: ")
        dosya.write(storage1.list[1])
        dosya.write("\n2- Quantity of M6 bolts: ")
        dosya.write(storage1.list[3])
        dosya.write("\n3- 0.4mm 1000x2000mm2  Quantity of 304 stainless steel sheet: ")
        dosya.write(storage1.list[5])
        dosya.write("\n\nThe person who made changes the list: ")
        dosya.write(name.a)
        dosya.write(" ")
        dosya.write(name.b)
        dosya.write("\n\n13.00  30/07/2023  Generated .txt output of new data.. Have a good day!")
        dosya.write("\n///////////////////////////////////////////////////////////////////////////////")
        dosya.close()
    else:
        print("Program terminated...")
except:
    print("Error...")
