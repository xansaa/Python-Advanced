size = int(input())
commands = input().split(", ")
matrix = []

for _ in range(size):
    row = list(input().strip())
    matrix.append(row)

direction_mapper = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

position = None
total_nuts = 0

for row_index in range(size):
    for col_index in range(size):
        if matrix[row_index][col_index] == "s":
            position = [row_index, col_index]

for current_com in commands:
    desired_row = position[0] + direction_mapper[current_com][0]
    desired_col = position[1] + direction_mapper[current_com][1]

    if not (0 <= desired_row < size and 0 <= desired_col < size):
        print("The squirrel is out of the field.")
        print(f"Hazelnuts collected: {total_nuts}")
        exit()

    symbol = matrix[desired_row][desired_col]

    if symbol == "h":
        total_nuts += 1
        matrix[desired_row][desired_col] = "*"
        if total_nuts == 3:
            print("Good job! You have collected all hazelnuts!")
            print(f"Hazelnuts collected: {total_nuts}")
            exit()

    elif symbol == "t":
        print("Unfortunately, the squirrel stepped on a trap...")
        print(f"Hazelnuts collected: {total_nuts}")
        exit()

    position = [desired_row, desired_col]

print("The squirrel hasn’t collected all hazelnuts.")
print(f"Hazelnuts collected: {total_nuts}")
