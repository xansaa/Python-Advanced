def is_coordinate_valid(r1, c1, r2, c2, r, c):
    return 0 <= r1 < r and 0 <= r2 < r and 0 <= c1 < c and 0 <= c2 < c


rows, cols = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

while True:
    line = input()
    if line == "END":
        break

    command = line.split()
    if command[0] != 'swap' or len(command) != 5:
        print("Invalid input!")
        continue

    row1, col1, row2, col2 = [int(x) for x in command[1:]]
    if is_coordinate_valid(row1, col1, row2, col2 ,rows, cols):
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        [print(*row) for row in matrix]

    else:
        print("Invalid input!")

