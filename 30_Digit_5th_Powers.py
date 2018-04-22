import math


power_list = set()
for i in range( int(math.pow(9, 5)) * 6, 1,-1):

    power_sum = 0

    for num in str(i):

        power_sum += math.pow(int(num), 5)
        if power_sum > i:
            break

    if power_sum == i:
        power_list.add(i)


print(power_list)
print(sum(power_list))

