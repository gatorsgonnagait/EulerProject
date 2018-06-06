import Euler_Tools as et


def generate_prime_list(limit):
    return  [i for i in range(limit) if et.is_prime(i) ]

def cumulative_sums_list(list):
    sum_list = []
    current_sum = 0
    for i in list:
        current_sum+=i
        sum_list.append(current_sum)

    return sum_list


def sum_of_consecutive_primes_equals_prime(prime):

    prime_list = []

    for i in range(1, prime):

        if et.is_prime(i):
            prime_list.append(i)
            total = sum(prime_list)
            if total == prime:
                #print(prime_list)
                return prime_list
            elif total > prime:

                for p in prime_list[:-1]:
                    prime_list.pop(0)
                    total = sum(prime_list)
                    if total == prime:
                        #print(prime_list)
                        return prime_list
    return prime_list


def most_consecutive_primes(limit):
    max_prime = 0
    length_of_max = 0
    for i in range(limit):
        if et.is_prime(i):
            #print(i)
            temp_len = len(sum_of_consecutive_primes_equals_prime(i))
            if  temp_len > length_of_max:
                max_prime = i
                length_of_max = temp_len

    return max_prime


def find_longest_prime_list(limit):
    prime_list = []
    for i in range(limit):
        if et.is_prime(i):
            prime_list.append(i)

    max_num_primes = 0
    max_prime = 0


    for j in range(len(prime_list), 1, -1):

        for i in range(len(prime_list)-1, 0, -1):
            print(i, j)
            sum_primes = sum(prime_list[i:j])
            if et.is_prime(sum_primes) and sum_primes < limit :
                print('sum of primes')
                print(sum_primes)
                if len(prime_list[i:j]) > max_num_primes :
                    max_num_primes = len(prime_list[i:j])
                    max_prime = sum_primes
                    print(max_prime)

    return max_prime, max_num_primes

def cumulative_primes(limit):
    prime_list = generate_prime_list(limit)
    sum_list = cumulative_sums_list(prime_list)
    max_num_primes = 0
    max_prime = 0

    for i in range(len(sum_list)-1, 1, -1):


        for j in range( len(sum_list)-1):
            print(i,j)
            total = sum_list[i] - sum_list[j]
            if total > limit:
                break
            if et.is_prime(total):
                if len(sum_list[j:i]) > max_num_primes:
                    max_num_primes = len(sum_list[j:i])
                    max_prime = total
                    print(max_prime)

    return max_prime, max_num_primes



print(cumulative_primes(1000000))

# print(most_consecutive_primes(1000))
#
# print(find_longest_prime_list(1000))
