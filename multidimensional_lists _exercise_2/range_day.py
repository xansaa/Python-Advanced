def move(direction, steps):
    r = my_pos[0] + (directions[direction][0] * int(steps))
    c = my_pos[1] + (directions[direction][1] * int(steps))

    if not (0 <= r < SIZE and 0 <= c < SIZE):
        return my_pos
    if matrix[r][c] == "x":
        return my_pos

    return [r, c]


def shoot(direction):
    r = my_pos[0] + directions[direction][0]
    c = my_pos[1] + directions[direction][1]

    while 0 <= r < SIZE and 0 <= c < SIZE:
        if matrix[r][c] == "x":
            matrix[r][c] = "."
            return [r, c]

        r += directions[direction][0]
        c += directions[direction][1]


SIZE = 5
matrix = []

targets = 0
targets_hits = 0
targets_hits_pos = []

my_pos = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(SIZE):
    matrix.append(input().split())

    if "A" in matrix[row]:
        my_pos = [row, matrix[row].index("A")]

    targets += matrix[row].count("x")

for _ in range(int(input())):
    command_info = input().split()

    if command_info[0] == "move":
        my_pos = move(command_info[1], command_info[2])
    elif command_info[0] == "shoot":
        targets_down_pos = shoot(command_info[1])

        if targets_down_pos:
            targets_hits_pos.append(targets_down_pos)
            targets_hits += 1

        if targets_hits == targets:
            print(f"Training completed! All {targets} targets hit.")
            break

if targets_hits < targets:
    print(f"Training not completed! {targets - targets_hits} targets left.")

print(*targets_hits_pos, sep='\n')
