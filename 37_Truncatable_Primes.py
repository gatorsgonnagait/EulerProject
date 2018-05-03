from Euler_Tools import is_prime

trunc_prime_set = set()

num = 10 # problem didnt want to include the single digit prime numbers
while(True):

    is_trunc_prime = False
    end = 0
    for index in range(len(str(num))):

        trunc_num_forwards = int(str(num)[index:])

        if end == 0:
            trunc_num_backwards = int(str(num))
        else:
            trunc_num_backwards = int(str(num)[:end])

        if is_prime( trunc_num_forwards ) and is_prime(trunc_num_backwards):
            is_trunc_prime = True
        else:
            is_trunc_prime = False
            break

        end -= 1

    if is_trunc_prime:
        trunc_prime_set.add(num)

    if len(trunc_prime_set)==11: # problem said there are only 11 truncatable primes
        break

    num+=1


print(trunc_prime_set)
print(sum(trunc_prime_set))


