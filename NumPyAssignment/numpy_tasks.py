import numpy as np

matrix = np.arange(2, 11).reshape(3, 3)
print("3x3 Matrix:\n", matrix)

user_input = input("Enter 4 numbers separated by space: ").split()
int_array = np.array(user_input, dtype=int)
float_array = int_array.astype(float)
print("Converted to float array:", float_array)

original_array = np.array([10, 20, 30])
appended_array = np.append(original_array, [40, 50, 60, 70, 80, 90])
print("Appended array:", appended_array)

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
sumArray = a + b
print("Sum of arrays:", sumArray)


array1 = np.arange(10, 100, 10).reshape(3, 3)
print("3x3 Array:\n", array1)
print("First row:", array1[0])
print("Last element:", array1[-1][-1])
