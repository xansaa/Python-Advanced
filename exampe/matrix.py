data = input().split(", ")
rows = int(data[0])
cols = int(data[1])

matrix = []

for _ in range(rows):
    elements = [int(el) for el in input().split(", ")]
    matrix.append(elements)