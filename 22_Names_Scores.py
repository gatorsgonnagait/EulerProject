def read_elements():
    with open('names.txt') as file:
        lines = file.readlines()
        return [ str[1:-1] for line in lines for str in line.split(',')]


def value_of_word(str):
    return sum( [ ord(letter.lower()) - 96 for letter in str] )


def sum_of_name_scores(sorted_names_list):
    total_sum = 0
    for i, name in zip( range(1, len(sorted_names_list)+1), sorted_names_list):
        total_sum += value_of_word(name)*i
    return total_sum
    # whats better for readability: the normal for loop, or the inline one below
    # return sum( [value_of_word(name) * i for i, name in zip( range(1, len(sorted_names_list)+1), sorted_names_list)])

print(value_of_word('colin'))
names_list = read_elements()
sorted_list = sorted(names_list)
print(sum_of_name_scores(sorted_list))