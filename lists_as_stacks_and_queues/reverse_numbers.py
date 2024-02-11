input_numbers = input()
numbers = input_numbers.split()
stack = []

for num in numbers:
    stack.append(num)

reverse_num = []
while stack:
    reverse_num.append(stack.pop())

print(" ".join(reverse_num))