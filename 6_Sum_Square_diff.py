import math
from itertools import  count, islice

def genNumberList(num):
    return [ c for c in islice(count(), num+1)]


def squareSum(listNums):
    sumNums = sum(listNums)
    return math.pow(sumNums, 2)

def sumSquare(listNums):
    sum = 0

    for num in listNums:
        sum += math.pow(num, 2)

    return sum

def difference(num):
    listNums = genNumberList(num)
    return squareSum(listNums) - sumSquare(listNums)


print(difference(100))