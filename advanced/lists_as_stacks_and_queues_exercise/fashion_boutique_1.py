clothes = [int(i) for i in input().split()]
capacity = int(input())

current_capacity = capacity
rack_counter = 1

while clothes:
    first_clothes = clothes[-1]
    if first_clothes > current_capacity:
        rack_counter += 1
        current_capacity = capacity
    else:
        current_capacity -= first_clothes
        clothes.pop()
print(rack_counter)