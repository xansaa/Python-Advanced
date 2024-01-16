rows = int(input())

matrix = []

for row in range(rows):
    elements = list(input())
    matrix.append(elements)

search_elements = input()
is_found = None
for row_index in range(rows):
    if is_found:
        break
    for col_index in range(len(matrix[row_index])):
        current_elements = matrix[row_index][col_index]
        if current_elements == search_elements:
            is_found = (row_index, col_index)
            print(is_found)
            break

if not is_found:
    print(f"{search_elements} does not occur in the matrix")
