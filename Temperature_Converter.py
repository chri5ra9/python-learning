#Temperature converter from Fahrenheit to Celsius

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