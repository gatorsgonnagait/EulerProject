fib = 3
first = 1
second = 2
sum = 2

while fib <= 4000000:
    if fib % 2 == 0:
        sum = sum + fib
    fib = first + second
    first = second
    second = fib

print(sum)