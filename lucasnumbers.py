x = int(input("What Lucas Number would you like to go up to? "))
count = 1
previous_num = 2
current_num = 1
print("2")
print("1")
while x-2>=count:
    temp = current_num
    current_num = current_num+previous_num
    print(current_num)
    count += 1
    previous_num = temp
print("This is the end of the Lucas Numbers up to "+str(x)+" .")