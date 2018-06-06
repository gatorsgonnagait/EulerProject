import Euler_Tools as et
import math

def twice_a_square(num):
    test = math.sqrt(num/2)
    return test == int(test)

def goldbachs_conjecture(num):

    for i in range(num):
        if not et.is_even(i) and et.is_prime(i):
            diff = num - i
            if twice_a_square(diff):
                return True
    return False


print(goldbachs_conjecture(1))

i = 3
while(True):

    if not et.is_prime(i) and not goldbachs_conjecture(i):
        break
    i+=2


print(i)