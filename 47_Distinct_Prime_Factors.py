import Euler_Tools as et



def distinct_prime_factors(num):

    factors = et.find_divisors(num)
    prime_factors = []
    for f in factors:
        if et.is_prime(f):
            prime_factors.append(f)

    return prime_factors

def consecutive_distinct_prime_factors(n):
    i = 0
    count = 0
    num_list = []
    while True:

        list = distinct_prime_factors(i)
        if len(list) == n:
            count+=1
            num_list.append(i)
        else:
            count = 0
            num_list.clear()

        if count == n:
            return num_list

        i+=1

print(consecutive_distinct_prime_factors(4))