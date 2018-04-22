import math

def distinct_powers(limit):
    power_set = set()

    for a in range(2, limit+1):

        for b in range(2, limit+1):

            power_set.add(math.pow(b,a))
            power_set.add(math.pow(a,b))

    return len(power_set)


print(distinct_powers(100))