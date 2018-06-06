import Euler_Tools as et


def string_exponents(num, power):
    product = num
    for i in range(1, power):
        product = et.multiply_two_numbers(product, num)
    return product

def last_n_digits_in_str_exponent(num, power, limit):
    product = num
    for i in range(1, power):
        product = et.multiply_two_numbers_last_n_digits(product, num, limit)
    return product



limit = 10
exp_list = []
for i in range(limit, 0, -1):
    print(i)
    exp_list.append(last_n_digits_in_str_exponent(i, i, 10))


str_sum = '0'
for str_num in exp_list:
    print(str_num)
    str_sum = et.add_two_numbers_as_string(str_sum, str_num)

print(str_sum)
print(str_sum[-10:])

# above doesnt work

# s = sum(exp_list)
# print(s)
# print(str(s)[-10:])


L = 1000
d = 10**10

s = sum(pow(n, n) for n in range(1, L+1))
print(str(s)[-10:])
