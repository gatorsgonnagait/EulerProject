import math

def is_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    elif is_even(num):
        return False

    i = 3
    while i <= math.sqrt(num):
        if num % i == 0:
            return False
        i += 2
    return True

def is_even(num):
    return True if num % 2 == 0 else False



def circular_primes_below_limit(limit):
    rotated_primes = []
    for i in range(limit):

        if i > 10 and is_prime(i):
            rotated_num = str(i)
            primes = True
            for j in range(len(rotated_num)-1):

                rotated_num =  rotated_num[-1] + rotated_num[:-1]
                if not is_prime(int(rotated_num)):
                    primes = False
                    break
            if primes:
                rotated_primes.append(int(rotated_num))
        else:
            if is_prime(i):
                rotated_primes.append(i)

    return rotated_primes


limit = 1000000

rotated_primes = circular_primes_below_limit(limit)
print(rotated_primes)
print(len(rotated_primes))

