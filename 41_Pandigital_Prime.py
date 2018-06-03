from Euler_Tools import is_prime
import itertools


def generate_pandigital_list(number):

    digit_set = set(itertools.permutations(str(number)))
    digit_list = []
    for num in digit_set:
        number = ''
        for digit in num:
            number += digit

        digit_list.append(int(number))

    return digit_list


def pandigital_number(n):
    digit = ''
    for i in range(n , 0, -1):
        digit += str(i)

    return int(digit)

def largest_pandigital_prime():

    for i in range(9, 0, -1):

        pan_number = pandigital_number(i)
        pan_list = sorted(generate_pandigital_list(pan_number),reverse=True)
        for num in pan_list:
            if is_prime(num):
                return num



num = pandigital_number(3)
print(num)

print(generate_pandigital_list(num))

print(largest_pandigital_prime())

