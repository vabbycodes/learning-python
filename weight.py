A=int(input("weight of the person in kg="))
B=int(input("height of the person in cm="))
BMI=((A*10000)/(B**2))
if BMI>=25:
        print("person is overweight")
else:
    print("you are not overweight ")
