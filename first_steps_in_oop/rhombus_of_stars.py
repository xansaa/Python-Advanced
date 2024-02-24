n = int(input())


def print_upper_rhombus(size):
    for row in range(1, n + 1):
        print(" " * (n - row), "* " * row)


def print_bottom_rhombus(size):
    for row in range(size - 1, 0, -1):
        print(" " * (n - row), "* " * row)


def print_rhombus(size):
    print_upper_rhombus(size)
    print_bottom_rhombus(size)


print_rhombus(n)
