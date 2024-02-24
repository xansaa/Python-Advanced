def get_next_pos(position, directions, direction, matrix):
    current_row, current_col = position
    row, col = directions[direction]
    next_row = current_row + row
    next_col = current_col + col
    if 0 <= next_row < len(matrix) and 0 <= next_col < len(matrix):
        return next_row, next_col

    if next_row < 0:
        next_row = len(matrix) - 1
    elif next_row >= len(matrix):
        next_row = 0

    if next_col < 0:
        next_col = len(matrix) - 1
    elif next_col >= len(matrix):
        next_col = 0

    return next_row, next_col


size = int(input())

matrix = []
total_fish = 0
position = None

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row_index in range(size):
    data = list(input())

    if "S" in data:
        col_index = data.index("S")
        position = [row_index, col_index]
    matrix.append(data)

command = input()

while command != "collect the nets":
    current_row_index, current_col_index = position
    next_row_index, next_col_index = get_next_pos(position, directions, command, matrix)

    symbol = matrix[next_row_index][next_col_index]
    matrix[next_row_index][next_col_index] = "S"
    matrix[current_row_index][current_col_index] = "-"
    position = [next_row_index, next_col_index]

    if symbol.isdigit():
        total_fish += int(symbol)

    elif symbol == "W":
        print(f'You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the '
              f'ship: [{position[0]},{position[1]}]')
        exit()

    command = input()

if total_fish >= 20:
    print("Success! You managed to reach the quota!")
else:
    print(f"You didn't catch enough fish and didn't reach the quota! "
          f"You need {20 - total_fish} tons of fish more.")
if total_fish > 0:
    print(f"Amount of fish caught: {total_fish} tons.")

for row_p in matrix:
    print(f"{''.join(row_p)}")
