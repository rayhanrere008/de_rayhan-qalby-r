def prime_rectangle(height, width, start):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def next_prime(num):
        while True:
            num += 1
            if is_prime(num):
                return num

    result = ""
    total_primes = 0
    current_num = start
    for i in range(height):
        row = ""
        for j in range(width):
            prime = next_prime(current_num)
            row += str(prime) + " "
            current_num = prime
            total_primes += prime
        result += row.strip() + "\n"
    result += str(total_primes)
    print(result)

# Test cases
prime_rectangle(2, 3, 13)
print()
prime_rectangle(5, 2, 1)