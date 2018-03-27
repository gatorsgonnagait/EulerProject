
num = 600851475143


def Greatest_Prime_Factors(num):
    factor = 2

    while factor < num:

        if num % factor == 0: # check the factors to see if theyre prime
            return Greatest_Prime_Factors(num/factor)
        factor +=1

    return num

print(Greatest_Prime_Factors(num))