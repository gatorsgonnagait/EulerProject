from Euler_Tools import read_nums, value_of_word


def triangle_number_set(n):
    list = []
    for i in range(1, n+1):
        list.append(i*(i+1)//2)
    return list

word_list = read_nums('common_words')
triangle_set = triangle_number_set(100)
triangle_word_count = 0

for word in word_list:

    if value_of_word(word[1:-1]) in triangle_set:
        triangle_word_count+=1


print(triangle_word_count)

