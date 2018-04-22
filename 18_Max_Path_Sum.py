

# had to look the good way to this problem. It involves filling out a grid with zeroes, adding them together and seeing which
# is the greatest sum
def read_nums():
    with open('67_numbers.txt') as file:
        lines = file.readlines()
        list_of_rows = []
        rows = []
        for line in lines:

            for num in line.split():

                rows.append(int(num))
            copy = list(rows)
            list_of_rows.append(copy)
            rows.clear()
        return list_of_rows


def add_zeros(triangle_grid):
    triangle_height = len(triangle_grid)
    for i, row in enumerate(triangle_grid):
        for j in range(i, triangle_height-1):
            row.append(0)
    return triangle_grid


def max_path_sum(triangle_grid):
    rev_grid = list(reversed(triangle_grid))

    for i, line in enumerate(rev_grid):

        for j in range(len(line)-i-1):
            row_up = rev_grid[i + 1][j]
            same_row_1 = rev_grid[i][j]
            same_row_2 = rev_grid[i][j+1]

            if row_up + same_row_1 > row_up + same_row_2:
                rev_grid[i + 1][j] = row_up + same_row_1
            else:
                rev_grid[i + 1][j] = row_up + same_row_2

    return rev_grid[-1][0]




grid = read_nums()
grid_w_zeroes = add_zeros(grid)

# answer 1074
print(max_path_sum(grid_w_zeroes))



