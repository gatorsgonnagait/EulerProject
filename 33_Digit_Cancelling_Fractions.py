from fractions import  Fraction

fraction_list = []
for i in range(10, 100):

    for j in range(10, 100):
        if j < i:

            cancel_numerator = int(str(j)[-1])
            cancel_denominator = int(str(i)[0])

            if int(str(i)[-1]) != 0 and cancel_numerator == cancel_denominator:
                if j/i == int(str(j)[0])/int(str(i)[-1]):
                    fraction_list.append([j,i])

product = 1
numerator = 1
denom = 1
for f in fraction_list:
    print(f)
    numerator *= f[0]
    denom *= f[1]

print(numerator)
print(denom)

print(Fraction(numerator, denom))

