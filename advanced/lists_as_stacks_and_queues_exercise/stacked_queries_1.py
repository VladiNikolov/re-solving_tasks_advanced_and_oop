number = int(input())

stack = []

while number > 0:
    input_line = input().split()
    if input_line[0] == "1":
        current_number = input_line[1]
        stack.append(int(current_number))
    elif input_line[0] == "2":
        if len(stack) > 0:
            stack.pop()
    elif input_line[0] == "3":
        if len(stack) > 0:
            print(max(stack))
    elif input_line[0] == "4":
        if len(stack) > 0:
            print(min(stack))
    number -= 1

reversed_stack = []
for _ in range(len(stack)):
    reversed_stack.append(str(stack.pop()))
print(", ".join(reversed_stack))
