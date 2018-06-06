import itertools, Euler_Tools as et

c = 0
for i in range(1000, 9999-3330-3330):
    if et.is_prime(i):
        num2 = i +3330
        num3 = num2 + 3330

        if et.is_prime(num2) and et.is_prime(num3):
            permutations = set(itertools.permutations(str(i)))

            if tuple(str(num2)) in permutations and tuple(str(num3)) in permutations :
                if  c == 1:
                    print(i, num2, num3)
                    break
                c+=1
