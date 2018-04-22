
def find_triple_given_sum(sum):
    a = 1
    while a <= sum/3:

        b = a + 1
        while b <= sum/2:

            c = sum - a - b
            print(c)
            if ( a*a + b*b == c*c):
                return a * b * c
            b+=1

        a+=1


print(find_triple_given_sum(1000))