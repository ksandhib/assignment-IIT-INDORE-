def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def get_primes_from_user():
    # Ask user how many numbers they want to enter
    n = int(input("How many numbers do you want to enter? "))
    numbers = []
    
    for i in range(n):
        val = int(input(f"Enter number {i+1}: "))
        numbers.append(val)
    
    print("\nPrime numbers in the list are:")
    for num in numbers:
        if is_prime(num):
            print(num)

if __name__ == "__main__":
    get_primes_from_user()
