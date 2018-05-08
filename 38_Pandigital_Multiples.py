from Euler_Tools import is_pandigital

pan_digital = set()
for i in range(100000):

    pan= ''
    for digit in range(1, 10):
        product = i * digit
        pan = pan + str(product)
        if len(pan)==9:
            if is_pandigital(pan):
                pan_digital.add(pan)
        elif len(pan)>9:
            break

print(pan_digital)
print(max(pan_digital))