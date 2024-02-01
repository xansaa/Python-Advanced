from functools import reduce


def operate(operator, *args):
    if operator == "+":
        return reduce(lambda x, y: x + y, args)
    if operator == "-":
        return reduce(lambda x, y: x - y, args)
    if operator == "*":
        return reduce(lambda x, y: x * y, args)
    if operator == "/":
        return reduce(lambda x, y: x / y, args)
