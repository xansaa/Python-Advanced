rows, cols = map(int, input().split(","))

matrix = []
mouse_pos = []

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

for row_index in range(rows):
    row = input()
    matrix.append(list(row))

    if "M" in row:
        col_index = row.index("M")
        mouse_pos = [row_index, col_index]
        matrix[mouse_pos[0]][mouse_pos[1]] = "*"

cheese_count = sum(row.count('C') for row in matrix)

while True:
    command = input()

    r, c = mouse_pos[0] + directions[command][0], mouse_pos[1] + directions[command][1]

    if not(0 <= r < rows and 0 <= c < cols):
        print("No more cheese for tonight!")
        matrix[mouse_pos[0]][mouse_pos[1]] = "M"
        break
    if command == "danger":
        print("Mouse will come back later!")
        matrix[r][c] = "M"
        break
    if matrix[r][c] == "C":
        cheese_count -= 1
        matrix[r][c] = "*"
        if cheese_count <= 0:
            matrix[r][c] = "M"
            print("Happy mouse! All the cheese is eaten, good night!")
            break
    if matrix[r][c] == "T":
        print("Mouse is trapped!")
        matrix[r][c] = "M"
        break
    if matrix[r][c] == "@":
        continue
    mouse_pos = [r, c]
[print(*el, sep='') for el in matrix]
