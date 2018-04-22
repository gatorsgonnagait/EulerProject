# this takes forever to run, it isnt optimized
num = 1
limit = 20
while True:

    divisors = 1
    print(num)
    while divisors < limit:
        if num % divisors != 0:
            #print(divisors)

            break
        divisors += 1

    print(divisors)
    if divisors == limit:
        print()
        print(num)
        break
    num +=1




