
print(format(585, 'b'))

def isPalidrome(number):
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

sum_list = []
for num in range(1000000):

    if isPalidrome(num) and isPalidrome(format(num, 'b')):

        sum_list.append(num)


print(sum_list)
print(sum(sum_list))