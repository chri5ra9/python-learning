#Temperature converter from Fahrenheit to Celsius
while True:
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9
    
    print ('the temperature in Celsius is  ' + str(int(celsius)))

    
    
    if celsius > 30:
        print ("it is hot outside")
    elif celsius >=20:
        print("it is warm outside")
    elif celsius >= 10:
        print("it is mild outside")
    else:
        print("it is cold outside")    


    print("--------------------------")
    print("1 - Convert another temperature")
    print("2 - Quit")
    print("--------------------------")

    choice = input("Choose and option: ")
    if choice == "1":
        pass

    elif choice == "2":
        break
    
    else:
        print("Invalid option — please enter 1, 2, or 3")

    

    