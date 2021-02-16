print("Welcome to the Giant Calculator!")
n = input("What is your name? ")
print(n+", would you like an age, interest, or grade calculator?")
c = int(input("Type 1 for an age calculator, 2 for an interest calculator, 3 for a distance calculator, or 4 for a grade calculator: "))

if c <= 1 :
    print("Welcome to the age calculator "+n+"!")

    age = int(input(n+", please Enter Your Age: "))

    if age >= 18:
        print(n+", you are an adult.")
    else:
        print(n+", you are a minor.")

elif c <= 2:
    print(n+", welcome to the Interest Calculator!")

    p = int(input(n+", enter your principle value: "))
    y = int(input(n+", enter the number of years you pay: "))
    r = int(input(n+", enter your interest rate: "))

    # to convert strings to integers, use int(), and to convert integers to string, use str()

    # interest = (principal value times number of years times rate of interest) all divided by 100
    i = (p * y * r) / 100

    interest = i-p

    u = str(interest)

    print(n + ", your interest is $" + u + "0")

elif c<=3:
    print("Welcome to the distance calculator!")

    k = input(n+", please enter your starting city: ")
    j = input(n+", please enter your destination: ")


    rate = int(input(n+", please enter the speed at which you will be travelling in miles: "))

    time1 = int(input(n+", please enter your starting time: "))
    time2 = int(input(n+", please enter your ending time: "))
    time3 = (12-time1)+(12-time2)

    distance = str(rate*time3)

    print(n+", the distance between "+k+" and "+j+" is "+distance+" miles.")

    response = int(input("Would you like to know this speed in kilometers too? Please enter a 1 for yes, or a 2 for no. "))

    if response <= 1:
        kilometers = int(distance)*1.609
        print(n + ", the distance between " + k + " and " + j + " is " + str(kilometers) + " kilometers.")

    elif response <= 2:
        print("Thank you for using the distance calculator!")


elif c <= 4:
    print("Welcome to the grade calculator!")

    marks = int(input("Please enter your marks " + n + ": "))

    if marks >= 97:
        print(n + ", your grade is an A+!")

    elif marks >= 93:
        print(n + ", your grade is an A!")

    elif marks >= 90:
        print(n + ", your grade is an A-!")

    elif marks >= 87:
        print(n + ", your grade is an B+!")

    elif marks >= 84:
        print(n + ", your grade is an B!")

    elif marks >= 80:
        print(n + ", your grade is an B-!")

    elif marks >= 77:
        print(n + ", your grade is an C+!")

    elif marks >= 73:
        print(n + ", your grade is an C!")

    elif marks >= 70:
        print(n + ", your grade is an C-!")

    elif marks >= 67:
        print(n + ", your grade is an D+!")

    elif marks >= 64:
        print(n + ", your grade is an D!")

    elif marks >= 60:
        print(n + ", your grade is an D-!")

    elif marks < 60:
        print(n + ", your grade is an F!")