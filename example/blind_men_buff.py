rows, cols = [int(x) for x in input().split()]

matrix = []
touched_opponents = 0
move_made = 0
position = []

for row in range(rows):
    col = input().split()
    matrix.append(col)

    if "B" in col:
        col_index = matrix[row].index("B")
        position = [row, col_index]
        matrix[position[0]][position[1]] = '-'

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

command = input()

while command != "Finish":
    r, c = position[0] + directions[command][0], position[1] + directions[command][1]

    if 0 <= r < rows and 0 <= c < cols:
        target = matrix[r][c]

        if target == "P":
            move_made += 1
            touched_opponents += 1
            matrix[r][c] = "-"
            position = [r, c]
            if touched_opponents == 3:
                break

        if target == "-":
            move_made += 1
            position = [r, c]

    command = input()

print("Game over!")
print(f"Touched opponents: {touched_opponents} Moves made: {move_made}")
