stack = []

number = int(input())

for _ in range(number):
    query_parts = [int(i) for i in input().split()]
    command = query_parts[0]
    if command == 1:
        add_number = query_parts[1]
        stack.append(add_number)
    elif command == 2 and stack:
        stack.pop()
    elif command == 3 and stack:
        print(max(stack))
    elif command == 4 and stack:
        print(min(stack))

reversed_stack = []

while stack:
    reversed_stack.append(str(stack.pop()))
print(", ".join(reversed_stack))