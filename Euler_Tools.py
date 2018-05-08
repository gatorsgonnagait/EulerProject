import math

def is_palidrome(number):
    i = 0
    end = -1
    palindrome = True
    while i < len(str(number)) / 2:
        if str(number)[i] != str(number)[end]:
            palindrome = False
            break
        i += 1
        end -= 1
    return palindrome

def is_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    elif is_even(num):
        return False

    i = 3
    while i <= math.sqrt(num):
        if num % i == 0:
            return False
        i += 2
    return True


def is_even(num):
    return True if num % 2 == 0 else False

def is_pandigital(n, s=9):
    n=str(n)
    return len(n)==s and not '1234567890'[:s].strip(n)