import math

def find_divisors(num):
    divisor = 1
    divisor_list = []
    while (divisor <= math.sqrt(num)):
        if num%divisor==0:
            if num/divisor == divisor:
                divisor_list.append(divisor)
            else:
                divisor_list.append(num//divisor)
                divisor_list.append(divisor)
        divisor += 1

    return divisor_list


def is_abundant(num):
   return sum(find_divisors(num)[1:]) > num

def sum_of_two_abundant_numbers(num):
    if num < 24:
        return False

    for i in range(12, num+1):
        if is_abundant(i) and is_abundant(num-i):

            return True

    return False

# takes a few minutes, i didn't figure out a more efficient way
def sum_of_non_abundant_numbers():
    return  sum( [i for i in range(1, 28124) if not sum_of_two_abundant_numbers(i) ] )

print(sum_of_non_abundant_numbers())