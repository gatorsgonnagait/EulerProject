
def reverse_string(str):
    return str[::-1]


def add_two_numbers_as_string(num1, num2):
    backwards_num_string1 = reverse_string(str(num1))
    backwards_num_string2 = reverse_string(str(num2))
    if len(backwards_num_string1) < len(backwards_num_string2):
        num_zeros = len(backwards_num_string2) - len(backwards_num_string1)
        backwards_num_string1 = backwards_num_string1 + '0' * num_zeros
    elif len(backwards_num_string1) > len(backwards_num_string2):
        num_zeros = len(backwards_num_string1) - len(backwards_num_string2)
        backwards_num_string2 = backwards_num_string2 + '0' * num_zeros

    carry_over = 0
    backwards_num_string_new = ''

    for i, digit1, digit2 in zip( range(0, len(backwards_num_string1)), backwards_num_string1, backwards_num_string2 ):

        int_digit = int(digit1) + int(digit2) + carry_over
        if int_digit > 9:
            if i == len(backwards_num_string1)-1:
                backwards_num_string_new = backwards_num_string_new + str(int_digit)[-1] + str(int_digit)[0]
                break
            carry_over = int_digit // 10
            int_digit = int_digit % 10
        else:
            carry_over = 0

        backwards_num_string_new = backwards_num_string_new[:i] + str(int_digit)
    return reverse_string(backwards_num_string_new)


#print(add_two_numbers_as_string(100, 200))

def multiply_two_numbers(num1, num2):
    backwards_num_string1 = reverse_string(str(num1))
    backwards_num_string2 = reverse_string(str(num2))
    product_lines = []

    for j, digit2 in zip( range(0, len(backwards_num_string2)), backwards_num_string2):
        carry_over = 0
        backwards_num_string_new = ''

        for i, digit1 in zip( range(0, len(backwards_num_string1)), backwards_num_string1):

            int_digit = int(digit1) * int(digit2) + carry_over

            if int_digit > 9:
                if i == len(backwards_num_string1) - 1:
                    backwards_num_string_new = backwards_num_string_new + str(int_digit)[-1] + str(int_digit)[0]
                    break
                carry_over = int_digit // 10
                int_digit = int_digit % 10
            else:
                carry_over = 0
            backwards_num_string_new = backwards_num_string_new[:i] + str(int_digit)
        print(reverse_string(backwards_num_string_new) + '0' * j)
        product_lines.append(reverse_string(backwards_num_string_new) + '0' * j)

    line_sum = 0
    if len(product_lines) > 1:
        for i in range(0, len(product_lines)-1):
            line_sum = add_two_numbers_as_string(product_lines[i], product_lines[i+1])
    else:
        line_sum = product_lines[0]

    return line_sum

print(multiply_two_numbers(2, 4))