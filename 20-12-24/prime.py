def is_prime(number):
    if number <= 1:
        return False
    for divisor in range(2, number):
        if number % divisor == 0:
            return False
    return True
   
   
def find_primes(limit):
    primes = []
    for candidate in range(2, limit + 1):
        if is_prime(candidate):
            primes.append(candidate)
    return primes


upper_limit = 50
prime_numbers = find_primes(upper_limit)
print(prime_numbers)
