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


n = 0
max_count = 0
value_a = 0
value_b = 0

for a in range(-1000, 1000):

    for b in range(-1000, 1001):

        while True:

            quad_prime = math.pow(n, 2) + a * n + b
            if not is_prime(quad_prime):

                if n > max_count:
                    value_a = a
                    value_b = b
                    max_count = n

                n = 0
                break
            print(quad_prime)
            n+=1

print()
print(max_count)
print(value_a)
print(value_b)
print(value_a*value_b)




