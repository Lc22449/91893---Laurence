def prime_generator():
    """Generates an infinite sequence of prime numbers."""
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

def is_prime(n):
    """Checks if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Example usage:
primes = prime_generator()
for _ in range(10):  # Print the first 10 prime numbers
    print(next(primes))