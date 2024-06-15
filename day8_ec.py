# Write a function called prime_numbers. This function asks the
# user to enter a number (an integer) as an argument and returns a
# list of all the prime numbers within its range. For example, if the
# user enters 10, your code should return [2, 3, 5, 7] as prime
# numbers.

def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_numbers():
    up_to_num = int(input("Plese input an integer: "))
    return [num for num in range(2, up_to_num+1) if is_prime(num)]

answer = prime_numbers()
print(answer)
