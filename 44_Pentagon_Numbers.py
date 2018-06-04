import math


def pentagon_set(n):
    return [ i * (3 * i -1) // 2 for i in range(1, n+1) ]

def pentagonal_test(num):
    inverse_funct = ( math.sqrt(24 * num + 1) + 1)  / 6
    return inverse_funct == int(inverse_funct)


pent_list = pentagon_set(1000)
print(pent_list)

def find_pair_pentagon_nums():
    i = 0
    while(True):
        i+=1
        n = i * (3 * i - 1) / 2
        for j in range(i-1, 0, -1):
            m = j * (3 * j - 1) / 2
            if pentagonal_test(n - m ) and pentagonal_test( n + m):
                return i, j, n-m



print(pentagonal_test(22))

print(find_pair_pentagon_nums())