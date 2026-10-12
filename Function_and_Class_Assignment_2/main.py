def factor(num):
    if num < 0:
        return "Factorial not defined for negative numbers"
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact


def check_string(s):
    if 's' in s or 'S' in s:
        print("The string is containing the letter 's'")
    else:
        print("The string doesn’t contain the letter 's'")


class Student:
    def fun1(self, value):
        self.data = value
        return self.data

    def message(self):
        print(f"User defined input: {self.data}")


double_num = lambda x: x * 2

# Task 5: Palindrome Check
def is_palindrome(s):
    if s.lower() == s[::-1].lower():
        print("The string is a palindrome")
    else:
        print("The string is not a palindrome")

if __name__ == "__main__":
  
    num = int(input("Enter a number to find its factorial: "))
    print(f"Factorial of {num} is {factor(num)}")

 
    user_str = input("\nEnter a string: ")
    check_string(user_str)

 
    student_obj = Student()
    val = input("\nEnter a value for Student class: ")
    student_obj.fun1(val)
    student_obj.message()


    num_to_double = int(input("\nEnter a number to double: "))
    print(f"Doubled value: {double_num(num_to_double)}")


    palindrome_str = input("\nEnter a string to check palindrome: ")
    is_palindrome(palindrome_str)
