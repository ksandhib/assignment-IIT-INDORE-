# main.py

# Taking user input
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))
c = int(input("Enter third number (c): "))

# Using if-else to find the greatest
if a >= b and a >= c:
    if a == b or a == c:
        print("Greatest number is:", a, "(There is a tie)")
    else:
        print("Greatest number is:", a)
elif b >= a and b >= c:
    if b == c:
        print("Greatest number is:", b, "(There is a tie)")
    else:
        print("Greatest number is:", b)
else:
    print("Greatest number is:", c)
