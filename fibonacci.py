#a series of numbers in which each number ( Fibonacci number ) is the sum of the two preceding numbers. The simplest is the series 1, 1, 2, 3, 5, 8, etc.

previous_number = 0

current_number = 1

count = 0

s = int(input("What number would you like to go up to: "))

print(previous_number)
print(current_number)

while count < s-2:
    temp = current_number
    current_number = previous_number + current_number
    print(current_number)
    previous_number = temp
    count += 1
