from collections import deque

quantity_food = int(input())
orders = deque([int(i) for i in input().split()])
print(max(orders))

while orders:
    first_order = orders[0]
    if quantity_food >= first_order:
        quantity_food -= first_order
        orders.popleft()
    else:
        break

if len(orders) == 0:
    print("Orders complete")
else:
    print(f'Orders left: {" ".join(map(str, orders))}')



