import Euler_Tools as et

def find_2nd_tri_pent_hex():
    i = 1
    count = 0
    while(True):
        i+=1
        tri = i * ( i + 1) / 2
        if et.pentagonal_test(tri) and et.hexagonal_test(tri):
            if count == 1:
                return tri
            count+=1


print(find_2nd_tri_pent_hex())