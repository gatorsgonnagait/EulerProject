

def is_pandigital(n, s=9):
    n=str(n)
    return len(n)==s and not '1234567890'[:s].strip(n)
# if length is equal to 9 and the remaining cut string is not empty



# to limit search space, I only need to multiply a 2 digit number x 3 digit number to get a 5 digit number
# or a 1 digit number by a 4 digit number to get a 4 digit number. Those would add up to 9 digits
# i couldnt figure this out aside from brute forcing it
pan_digital = set()
for i in range(2,  60):

    if i < 10:
        start = 1234
    else:
        start = 123
    for j in range(start, 10000//i):
        if is_pandigital(str(i) + str(j) + str(i*j)):
            pan_digital.add(i*j)
            print(i, j)
            print(str(i*j))
            print()

print(sum(pan_digital))