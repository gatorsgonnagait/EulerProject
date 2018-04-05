
def read_nums():
    with open('13_numbers.txt') as f:
        return [ c for line in f for c in line if c.isdigit() ]


def make_long_number_lists(long_number_list, digit_length ):
    list_of_sums = []

    big_digit = ''
    for i ,num in enumerate(long_number_list, start=1):

        big_digit = big_digit + num
        if i%digit_length==0:
            print(big_digit)
            print()
            list_of_sums.append(int(big_digit))
            big_digit = ''

    return list_of_sums

def get_first_n_digits(n, sum_num):
    first_n_digits = ''
    return  [first_n_digits + str(digit) for i, digit in enumerate( str(sum_num)) if i < n ]




raw_list = read_nums()
list_of_sums = make_long_number_lists(raw_list, 50)

sum_of_big_nums = sum(list_of_sums)

print(sum_of_big_nums)

print(get_first_n_digits(10, sum_of_big_nums))
# answer is 5537376230