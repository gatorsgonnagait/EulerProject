def isEven(num):
    return True if num%2==0 else False



def collatz_chain(num):
    collatz_list = [num]

    while num > 1:

        if isEven(num):
            num /= 2
        else:
            num = 3*num + 1

        collatz_list.append(num)

    return collatz_list




def count_collatz_chain(limit):
    max_length = 10
    starting = 0
    for i in range(limit, 0, -1):
        length = len(collatz_chain(i))
        if length > max_length:
            max_length = length
            starting = i
            print(max_length)
            print(starting)
            print()

    return starting


limit = 1000000

print(count_collatz_chain(limit))