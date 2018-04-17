import math

def find_divisors(num):
    divisor = 1
    divisor_list = []
    while (divisor <= math.sqrt(num)):
        if num%divisor==0:
            if num/divisor == divisor:
                divisor_list.append(divisor)
            else:
                divisor_list.append(num//divisor)
                divisor_list.append(divisor)
        divisor += 1

    return divisor_list


def is_amicable(num):
    amicable_list = []
    amicable_test = sum(find_divisors(num)) - num
    amicable_test2 = sum(find_divisors(amicable_test)) - amicable_test

    if num == amicable_test2 and num != amicable_test:
        amicable_list.append(amicable_test)
        amicable_list.append(amicable_test2)

    return amicable_list


if __name__ == '__main__':

    amicable_set = set()
    for i in range(10000):
        amicable_list = is_amicable(i)
        if len(amicable_list) == 2:
            amicable_set.add(amicable_list[0])
            amicable_set.add(amicable_list[1])

    print(amicable_set)
    print(sum(amicable_set))
    # answer is 31626