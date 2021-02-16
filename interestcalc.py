q = input("Welcome to Krithik's Interest Calculator! What is your name? ")

p = int(input("Enter Your Principal Value: "))
y = int(input("Enter The Number Of Years You Pay: "))
r = int(input("Enter Your Interest Rate: "))

# to convert strings to integers, use int(), and to convert integers to string, use str()

# interest = (principal value times number of years times rate of interest) all divided by 100
i = (p*y*r)/100

u = str(i)

print(q+", your interest is $"+u+"0")