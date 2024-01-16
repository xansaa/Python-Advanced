rows = int(input())

matrix = []

for row in range(rows):
    elements = [int(el) for el in input().split(", ")]
    matrix.append(elements)

flattening = []

for row_index in range(rows):
    for col_index in range(len(matrix[row_index])):
        flattening.append(matrix[row_index][col_index])

print(flattening)
