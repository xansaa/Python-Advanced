data = input().split()
rows, cols = map(int, data)
snake_str = input()

matrix = [[' ' for _ in range(cols)] for _ in range(rows)]

current_index = 0
for row in range(rows):
    if row % 2 == 0:
        for col in range(cols):
            matrix[row][col] = snake_str[current_index % len(snake_str)]
            current_index += 1
    else:
        for col in range(cols - 1, -1, -1):
            matrix[row][col] = snake_str[current_index % len(snake_str)]
            current_index += 1


for row in matrix:
    print(''.join(row))