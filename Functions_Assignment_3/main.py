# Assignment 3 – Functions
# Python for Data Science Certification Course

# Task 1: Super class
class Super:
    def fun1(self):
        print("This is function 1 in the Super class.")

# Task 2: Modified_Super class inheriting from Super
class Modified_Super(Super):
    def fun1(self):
        print("This is function 1 in the Modified Super class.")

    def fun2(self):
        print("This is the 2nd function from the Modified Super class.")

# Task 3: Two Hello methods (method overloading simulation using default arguments)
def Hello(arg1, arg2=None):
    if arg2 is None:
        print("This function is only having 1 argument")
    else:
        print("This function is having 2 arguments")

# Task 4: Sum function accepting multiple inputs
def Sum(*args):
    total = 0
    for num in args:
        total += num
    return total

# Task 5: Encapsulation
class Encapsulation:
    def __init__(self):
        self.originalValue = 10

    def Value(self):
        return self.originalValue

    def setValue(self, newValue):
        self.originalValue = newValue


# ---------------- Main Execution ----------------
if __name__ == "__main__":
    # Task 1 & 2
    print("\n--- Task 1 & 2 ---")
    obj = Modified_Super()
    obj.fun1()
    obj.fun2()

    # Task 3
    print("\n--- Task 3 ---")
    Hello("Argument1")
    Hello("Argument1", "Argument2")

    # Task 4
    print("\n--- Task 4 ---")
    print("Sum of numbers (10, 20, 30):", Sum(10, 20, 30))

    # Task 5
    print("\n--- Task 5 ---")
    encap = Encapsulation()
    print("Original value:", encap.Value())
    encap.setValue(50)
    print("Updated value:", encap.Value())
