
def reverse_string(str):
    return str[::-1]

def convert_string_num_to_list(num):
    return [ int(digit)  for digit in num if digit.isdigit()]

# this is a kinda janky way of going about it. this only doubles numbers
# i didnt make it sum two different numbers which would be more versatile
def double_number_as_string(num):
    backwards_num_string = reverse_string(str(num))
    carry_over = 0
    backwards_num_string_new = ''

    for i, digit in enumerate(backwards_num_string):
        int_digit = int(digit) * 2 + carry_over
        if int_digit > 9:
            if i == len(backwards_num_string)-1:
                backwards_num_string_new = backwards_num_string_new + str(int_digit)[-1] + str(int_digit)[0]
                break
            carry_over = int_digit // 10
            int_digit = int_digit % 10
        else:
            carry_over = 0
        backwards_num_string_new = backwards_num_string_new[:i] + str(int_digit) 
    return reverse_string(backwards_num_string_new)


def square_number_n_times(num, n):
    for i in range(1, n):
        num = double_number_as_string(num)
    return num


print(double_number_as_string(2))
big_square = square_number_n_times(2, 1000)
print(big_square)
list = convert_string_num_to_list(big_square)
print(sum(list))



