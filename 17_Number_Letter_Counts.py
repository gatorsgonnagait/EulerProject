import math

def digit_string_length(digit):
    switcher = {
        1: 3,
        2: 3,
        3: 5,
        4: 4,
        5: 4,
        6: 3,
        7: 5,
        8: 5,
        9: 4,
        10: 3,
        11: 6, #eleven
        12: 6, #twelve
        13: 8, # thirteen
        14: 8,
        15: 7, #fifteen
        16: 7, # sixteen
        17: 9, # seventeen
        18: 8, # eighteen
        19: 8, # nineteen
        20: 6, # twenty
        30: 6, # thirty
        40: 5, # forty
        50: 5, # fifty
        60: 5, # sixty
        70: 7, # seventy
        80: 6, # eighty
        90: 6, # ninety
        100: 7,# hundred
        1000: 8,  # thousand
        1000000: 7# million
    }
    return switcher.get(digit)

#
def letter_counter(num): # includes 'and'
    number_length = len(str(num))
    str_num = str(num)
    and_length = 0
    counter = 0
    for i, j, digit in zip(range(number_length-1, -1, -1), range(number_length), str_num):
        if i > 1:
            if digit == '0': # if the number is 1002, skips the hundreds spot
                continue

            and_length = 3 # accounts for the 'and' needed after one hundred AND 1
            num_count = digit_string_length(int(digit)) #five
            counter += num_count
            place_count = digit_string_length(math.pow(10, i))# hundred
            counter += place_count
        else:
            tens = int(str_num[j:])

            if tens > 19:
                counter += and_length + digit_string_length(int(digit)*10)
                and_length = 0
            elif tens > 0:
                counter += and_length + digit_string_length(tens)
                break
            else:
                break
    return counter


print(letter_counter(342))

counter = 0
for i in range(1, 1001):
    counter += letter_counter(i)

print(counter)
