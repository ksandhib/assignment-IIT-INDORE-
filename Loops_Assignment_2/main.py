# Assignment 2 – Loops
# Task: Print even numbers from a given list using while loop

def print_even_numbers():
    numbers = [10, 23, 4, 26, 4, 75, 24, 54]
    index = 0
    while index < len(numbers):
        if numbers[index] % 2 == 0:
            print(numbers[index])
        index += 1

if __name__ == "__main__":
    print_even_numbers()
