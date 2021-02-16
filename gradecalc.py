name = str(input("Welcome to the grade calculator! What is your name? "))
marks = int(input("Please enter your marks "+name+": "))
if marks >= 97:
    print(name+", your grade is an A+!")
elif marks >= 93:
    print(name+", your grade is an A!")
elif marks >= 90:
    print(name+", your grade is an A-!")
elif marks >= 87:
    print(name+", your grade is an B+!")
elif marks >= 84:
    print(name+", your grade is an B!")
elif marks >= 80:
    print(name+", your grade is an B-!")
elif marks >= 77:
    print(name+", your grade is an C+!")
elif marks >= 73:
    print(name+", your grade is an C!")
elif marks >= 70:
    print(name+", your grade is an C-!")
elif marks >= 67:
    print(name+", your grade is an D+!")
elif marks >= 64:
    print(name+", your grade is an D!")
elif marks >= 60:
    print(name+", your grade is an D-!")
elif marks < 60:
    print(name+", your grade is an F!")