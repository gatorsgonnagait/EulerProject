
def reverse_string(str):
    return str[::-1]

# handles the carry over operation when manually adding or multiplying
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


print(add_two_numbers_as_string(11, 999))

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

print(multiply_two_numbers(4, 32))

def manual_factorial(limit):
    product = '1'
    for i in range(1, limit):
        product = multiply_two_numbers(int(product), i + 1)
    return product

def sum_of_nums_in_string(number_string):
    return sum( [ int(d) for d in number_string] )


if __name__ == '__main__':

    limit = 100
    factorial = manual_factorial(limit)
    print(factorial)
    print(sum_of_nums_in_string(factorial))
    # answer is 648
