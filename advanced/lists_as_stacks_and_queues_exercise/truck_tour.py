from collections import deque

petrol_pumps = int(input())
pumps = deque()

for _ in range(petrol_pumps):
    pumps.append([int(i) for i in input().split()])

for index in range(petrol_pumps):
    trunk = 0
    failed = False
    for petrol, distance in pumps:
        trunk = trunk + petrol - distance
        if trunk < 0:
            failed = True
            break

    if failed:
        pumps.append(pumps.popleft())
    else:
        print(index)
        break
