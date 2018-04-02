import math
#not using this one
def get_triangle_number(nth_term):
    i = nth_term
    current_sum = 0
    while(i > 0):
        current_sum = current_sum + i
        i -= 1
    return current_sum

def find_num_divisors(num):
    divisor = 1
    num_divisors = 0
    #if num%2 == 1: # is odd
    while (divisor <= math.sqrt(num)):
        if num%divisor==0:

            if num/divisor == divisor:
                num_divisors += 1
            else:
                num_divisors +=2
        divisor += 1

    return num_divisors

def generate_triangle_nums(divisors_limit):
    i = 1
    current_sum = 0

    while(True):
        num_of_divisors = find_num_divisors(current_sum)
        print('triangle number ' + str(current_sum))
        print('number of divisors ' + str(num_of_divisors))
        print()
        if num_of_divisors >= divisors_limit:

            return current_sum
        current_sum += i
        i += 1



print(find_num_divisors(100))

divisors_limit = 500
print(generate_triangle_nums(divisors_limit))

# answer is 76576500