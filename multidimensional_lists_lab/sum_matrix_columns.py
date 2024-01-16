data = input().split(", ")
rows = int(data[0])
cols = int(data[1])

matrix = []

for row in range(rows):
    elements = [int(el) for el in input().split()]
    matrix.append(elements)

for col_index in range(cols):
    sum_cols_nums = 0
    for row_index in range(rows):
        sum_cols_nums += matrix[row_index][col_index]
    print(sum_cols_nums)