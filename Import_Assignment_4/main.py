import Module
from Module import addition
from Module import subtraction
from Module import multiplication, division


print("Using import Module:")
print("Addition:", Module.addition(10, 5))
print("Subtraction:", Module.subtraction(10, 5))
print("Multiplication:", Module.multiplication(10, 5))
print("Division:", Module.division(10, 5))


print("\nUsing 'from Module import addition':")
print("Addition:", addition(20, 10))


print("\nUsing 'from Module import subtraction':")
print("Subtraction:", subtraction(50, 25))

print("\nUsing 'from Module import multiplication, division':")
print("Multiplication:", multiplication(7, 6))
print("Division:", division(42, 7))
