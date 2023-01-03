from collections import deque

total_water = int(input())
people = deque()

while True:
    command = input()
    if command == "Start":
        break
    people.append(command)

while True:
    command = input()
    if command == "End":
        break
    current_command = command.split()
    if len(current_command) == 2:
        total_water += int(current_command[1])
    else:
        person_name = people.popleft()
        litters = int(current_command[0])
        if total_water >= litters:
            print(f"{person_name} got water")
            total_water -= litters
        else:
            print(f"{person_name} must wait")

print(f"{total_water} liters left")




