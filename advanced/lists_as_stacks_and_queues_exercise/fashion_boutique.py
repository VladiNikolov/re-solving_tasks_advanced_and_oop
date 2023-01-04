clothes = [int(i) for i in input().split()]
capacity = int(input())
current_capacity = capacity
rack = 1

while clothes:
    first_clothes = clothes.pop()

    if current_capacity - first_clothes >= 0:
        current_capacity -= first_clothes
        continue
    else:
        clothes.append(first_clothes)
        rack += 1
        current_capacity = capacity

print(rack)
