

print("Hello,")
print("one kilometer today equals exactly 0.621371 miles.")
print("Would you like to convert kilometers into miles?")
print("This converter helps you.")
print("")

while True:
    convert = int(input("Kilometer: "))

    mile = convert * 0.621371

    print("Meilen: ", mile)

    a = input("Do you want to start another conversion? Y/N   ")

    if a == str("N") or str("n"):              
        print("Thanks for using")
        break
    else:
        print("")


