from collections import deque

water_in_dispenser = int(input())

input_line = input()
people_deque = deque()

while input_line != "Start":
    people_deque.append(input_line)

    input_line = input()

input_line = input()
while input_line != "End":
    line = input_line.split()

    if line[0] == "refill":
        water_in_dispenser += int(line[1])
    else:
        person_name = people_deque.popleft()
        litters = int(line[0])
        if water_in_dispenser >= litters:
            water_in_dispenser -= litters
            print(f"{person_name} got water" )
        else:
            print(f"{person_name} must wait" )

    input_line = input()

print(f"{water_in_dispenser} liters left")




