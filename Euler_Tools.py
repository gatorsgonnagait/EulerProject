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


def permutate(seq):
    if not seq:
        return [seq]

    temporary = []
    for i in range(len(seq)):
        for j in permutate(seq[: i] + seq[i + 1:]):
            temporary.append(seq[i: i + 1] + j)
    return temporary

def triangular_test(num):
    inverse = ( math.sqrt( 8 * num + 1) - 1) / 2
    return inverse == int(inverse)

def pentagonal_test(num):
    inverse = ( math.sqrt(24 * num + 1) + 1)  / 6
    return inverse == int(inverse)

def hexagonal_test(num):
    inverse = ( math.sqrt( 8 * num + 1) + 1) / 4
    return inverse == int(inverse)

def twice_a_square(num):
    test = math.sqrt(num/2)
    return test == int(test)

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

def reverse_string(str):
    return str[::-1]


def carry_over(int_digit, carry, backwards_num, str_length, pos):

    if int_digit > 9:
        if pos == str_length - 1:
            return backwards_num + str(int_digit)[-1] + str(int_digit)[0] , int_digit, carry
        carry = int_digit // 10
        int_digit = int_digit % 10
    else:
        carry = 0
    return backwards_num[:pos] + str(int_digit), int_digit, carry

def str_length_diff(str1, str2):
    return len(str1) - len(str2)

def add_two_numbers_as_string(num1, num2):
    backwards_num_string1 = reverse_string(str(num1))
    backwards_num_string2 = reverse_string(str(num2))

    if len(backwards_num_string1) < len(backwards_num_string2):
        num_zeros = str_length_diff(backwards_num_string2, backwards_num_string1)
        backwards_num_string1 = backwards_num_string1 + '0' * num_zeros
    elif len(backwards_num_string1) > len(backwards_num_string2):
        num_zeros = str_length_diff(backwards_num_string1, backwards_num_string2)
        backwards_num_string2 = backwards_num_string2 + '0' * num_zeros

    carry = 0
    backwards_num_string_new = ''

    for i, digit1, digit2 in zip( range(0, len(backwards_num_string1)), backwards_num_string1, backwards_num_string2 ):

        int_digit = int(digit1) + int(digit2) + carry
        backwards_num_string_new, int_digit, carry = carry_over(int_digit, carry, backwards_num_string_new, len(backwards_num_string1), i)

    return reverse_string(backwards_num_string_new)



def multiply_two_numbers(num1, num2):
    backwards_num_string1 = reverse_string(str(num1))
    backwards_num_string2 = reverse_string(str(num2))
    product_lines = []

    for j, digit2 in zip( range(0, len(backwards_num_string2)), backwards_num_string2):
        carry = 0
        backwards_num_string_new = ''

        for i, digit1 in zip( range(0, len(backwards_num_string1)), backwards_num_string1):

            int_digit = int(digit1) * int(digit2) + carry
            backwards_num_string_new, int_digit, carry = carry_over(int_digit, carry, backwards_num_string_new, len(backwards_num_string1), i)
        product_lines.append(reverse_string(backwards_num_string_new) + '0' * j)

    line_sum = 0
    if len(product_lines) > 1:
        for i in range(0, len(product_lines)-1):
            line_sum = add_two_numbers_as_string(product_lines[i], product_lines[i+1])
    else:
        line_sum = product_lines[0]

    return line_sum

def multiply_two_numbers_last_n_digits(num1, num2, digit_limit):
    backwards_num_string1 = reverse_string(str(num1))
    backwards_num_string2 = reverse_string(str(num2))
    product_lines = []

    for j, digit2 in zip( range(0, len(backwards_num_string2)), backwards_num_string2):
        carry = 0
        backwards_num_string_new = ''
        line = ''
        for i, digit1 in zip( range(0, len(backwards_num_string1)), backwards_num_string1):

            int_digit = int(digit1) * int(digit2) + carry
            backwards_num_string_new, int_digit, carry = carry_over(int_digit, carry, backwards_num_string_new, len(backwards_num_string1), i)
            line = reverse_string(backwards_num_string_new) + '0' * j
            if len(line)>digit_limit:
                #line = line[:digit_limit]
                break
        product_lines.append(line)

    line_sum = 0
    if len(product_lines) > 1:
        for i in range(0, len(product_lines)-1):
            line_sum = add_two_numbers_as_string(product_lines[i], product_lines[i+1])
    else:
        line_sum = product_lines[0]

    return line_sum


def manual_factorial(limit):
    product = '1'
    for i in range(1, limit):
        product = multiply_two_numbers(int(product), i + 1)
    return product



