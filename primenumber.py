number = int(input("Please enter a number: "))
x = 2
while x < number:
    y = number % x
    if y == 0:
        print("This is not a prime number. ")
        break
    x += 1

if x == number:
    print("This is a prime number.")