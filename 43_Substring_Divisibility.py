from Euler_Tools import generate_pandigital_list, pandigital_number

pandigital_num = pandigital_number(9, True)

print(pandigital_num)

pan_list = generate_pandigital_list(pandigital_num)

print(pan_list)


sub_pans = []

for p in pan_list:

    if int(p[1:4])%2 == 0 :
        if int(p[2:5])%3 == 0:
            if int(p[3:6])%5 == 0:
                if int(p[4:7])%7 == 0:
                    if int(p[5:8])%11 == 0:
                        if int(p[6:9])%13 == 0:
                            if int(p[7:10])%17 == 0:
                                sub_pans.append(int(p))


print(sub_pans)
print(sum(sub_pans))