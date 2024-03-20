from math import isqrt


def get_primes(numbers: list):
    for number in numbers:
        if number <= 1:
            continue

        for divisor in range(2, isqrt(number) + 1):
            if number % divisor == 0:
                break
        else:
            yield number
