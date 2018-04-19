import math

# i honestly dont understand this one this well. I had to look up
# the solution and i dont even understand that.
# this somehow makes it work though using factorials and finding the
# remainder from whats left of the goal number

# find millionth permutation
nth_num = 1000000-1 # i guess because its zero based?

digit_list = []
remaining_nums = [0,1,2,3,4,5,6,7,8,9]

for i in reversed(range(len(remaining_nums))):

    factorial = math.factorial(i)
    place = nth_num // factorial
    digit = remaining_nums.pop(place)
    digit_list.append(digit)
    rem = nth_num - place * factorial
    nth_num = rem

print(digit_list)