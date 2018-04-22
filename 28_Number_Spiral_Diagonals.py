
def sum_spiral_diagonals(square_side):

    nums = 1
    skip = 2
    sum = 1
    i = 3
    while i <= square_side:

        for j in range(4):

            nums += skip
            sum += nums
            print(sum)
        print('end of square')
        skip+=2
        i+=2

    return sum


print(sum_spiral_diagonals(1001))


