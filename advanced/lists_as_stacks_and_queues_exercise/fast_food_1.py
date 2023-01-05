from collections import deque

food = int(input())
orders = deque([int(i) for i in input().split()])
print(max(orders))

for _ in range(len(orders)):
    if food < orders[0]:
        break
    else:
        first_order = orders.popleft()
        food -= first_order

if orders:
    print(f'Orders left: {" ".join(map(str, orders))}')
else:
    print("Orders complete")
