
def fibonacci(n):

    array = [0,1]
    for i in range(2, n+1):

        array.append( array[i-1] + array[i-2] )

    return  array[n]


def find_nth_digit_length(n):

    i = 0
    while True:

        fib_answer = fibonacci(i)
        if len(str(fib_answer)) == n:
            return i
        i+=1



print(find_nth_digit_length(1000))