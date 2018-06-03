import math, itertools

def is_palidrome(number):
    i = 0
    end = -1
    palindrome = True
    while i < len(str(number)) / 2:
        if str(number)[i] != str(number)[end]:
            palindrome = False
            break
        i += 1
        end -= 1
    return palindrome

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

def is_pandigital(n, s=9):
    n=str(n)
    return len(n)==s and not '1234567890'[:s].strip(n)


def is_pythagorean_triple(num):
    a = 1
    while a <= num / 3:
        b = a + 1
        while b <= num / 2:
            if (a * a + b * b == num):
                return a, b, int(math.sqrt(num))
            b += 1
        a += 1
    return False

def multiply_list(list):
    product = 1
    for item in list:
        product *= item
    return product


def read_nums(filename):
    with open(filename+'.txt') as f:
        return [ c for line in f for c in line.split(',') ]

def value_of_word(str):
    return sum( [ ord(letter.lower()) - 96 for letter in str] )

def generate_pandigital_list(number):

    digit_set = set(itertools.permutations(str(number)))
    digit_list = []
    for num in digit_set:
        num_str = ''
        for digit in num:
            num_str += digit

        digit_list.append(num_str)

    return digit_list


def pandigital_number(n, zero):
    digit = ''
    if zero:
        one = 1
    else:
        one = 0
    for i in range(n , 0-one, -1):
        digit += str(i)

    return digit
