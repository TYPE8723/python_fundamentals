# A prime number is a whole number greater than 1 that has only two factors: 1 and itself. For example, the first few prime numbers are 2, 3, 5, 7, 11, 13, 17, 19, and so on.

# To check whether a number is prime or not, we can use a simple method called trial division. Here's how it works:

# Take the number you want to check, say 7.
# Start dividing it by all the numbers from 2 to one less than the number itself (in this case, 2 to 6).
# If any of the divisions result in an exact quotient (with no remainder), then the number is not prime. Otherwise, the number is prime.

def is_prime(n):
    if n <= 1:
        # 1 and below are not prime
        return False
    for i in range(2, n):
        if n % i == 0:
            # n is divisible by i, so it's not prime
            return False
    # If we've gone through all the possible divisors and n is not divisible by any of them, then n is prime
    return True

for i in range(1,20):
    if is_prime(i) :
        print(f"{i} is prime")
    else:
        print(f"{i} is not prime")
