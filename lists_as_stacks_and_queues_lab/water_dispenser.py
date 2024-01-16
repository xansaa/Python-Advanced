from collections import deque

water = int(input())

name = input()
people = deque()

while name != "Start":
    people.append(name)
    name = input()

command = input()

while command != "End":
    data = command.split()
    if len(data) == 1:
        liters_request = int(data[0])
        person = people.popleft()

        if water >= liters_request :
            print(f"{person} got water")
            water -= liters_request
        else:
            print(f"{person} must wait")
    else:
        _, liters_to_add = data
        water += int(liters_to_add)

    command = input()

print(f"{water} liters left")