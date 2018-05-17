# this problem is insane

import math
from fractions import Fraction

from Euler_Tools import multiply_list

digit_length = 2
count = 9
total_digits = 0
# digit length powers of 10:  1 2 3 4 5 6 7
# numbers per step
# 9, 90, 900, 9000, 90000, 900000, 9000000
# find 1st, 10th, 100th, 1000th, 10,000th, 100,000th, 1 millionth digit
# digit 1 , 11,

digit_list = []
prev = 9
prev_total = 9
for i in range(1, 7):

    for j in range ( int(math.pow(10, i)), int(math.pow(10, i+1)) ) :

        if j == math.pow(10, i):

            print(j,'-', prev, '/', len(str(j - prev)),'+', prev_total)
            number = (j - prev) /len(str(j - prev)) + prev_total
            print(number)
            print(j)
            print()
            if not number.is_integer():

                number_dec = str(number - int(number))[1:]
                fraction = Fraction(float(number_dec)).limit_denominator()
                print(fraction)
                print(str(fraction)[0])
                number_place = int(str(fraction)[0])-1
            else:
                number_place = 0

            prev = count
            prev_total = j -1

            print(number_place)
            print(int(str(int(number))))
            print(int(str(int(number))[number_place]))
            digit_list.append(int(str(int(number))[number_place]))

        count += digit_length

    digit_length+=1
    print()


print(digit_list)
print(multiply_list(digit_list))

