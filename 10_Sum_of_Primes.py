
def is_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    elif is_even(num):
        return False

    i = 3
    while i <= num/3:
        if num % i == 0:
            return False
        i += 2
    return True

def is_even(num):
    return True if num % 2 == 0 else False


def sum_of_primes_below(limit):
    #sum = 0
    list_of_primes = []
    for num in range(limit):
        if is_prime(num):
            #sum += num
            list_of_primes.append(num)
            print(num)
    return sum(list_of_primes)

limit = 2000000
print(sum_of_primes_below(limit))
# takes forever. answer is 142,913,828,922