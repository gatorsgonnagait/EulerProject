digit_factorial = {
        0:1,
        1:1,
        2:2,
        3:6,
        4:24,
        5:120,
        6:720,
        7:5040,
        8:40320,
        9:362880
    }

upper_limit = digit_factorial[9]*7
factorial_equal_list = []

for num in range(10, upper_limit):

    fact_sum = 0
    for digit in str(num):
        fact_sum+= digit_factorial[int(digit)]
        if fact_sum > num:
            break
        elif fact_sum == num:
            factorial_equal_list.append(num)

print(factorial_equal_list)
print(sum(factorial_equal_list))
