def list_pythagorean_triples_given_sum(sum):
    triple_list = []
    a = 1
    while a <= sum/3:
        b = a + 1
        while b <= sum/2:
            c = sum - a - b
            if ( a*a + b*b == c*c):

                triple_list.append([a, b, c])
            b+=1
        a+=1
    return triple_list


limit = 1001
def most_triples_given_sum(limit):
    max_length = 0
    num = 0
    for i in range(limit):
        trip = list_pythagorean_triples_given_sum(i)
        if len(trip) > max_length:
            max_length = len(trip)
            num = i
    return num

print(most_triples_given_sum(limit))