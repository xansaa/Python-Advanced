rows = int(input())

matrix = []

for row_index in range(rows):
    elements =[int(el) for el in  input().split(", ") if int(el) % 2 == 0]
    matrix.append(elements)

print(matrix)