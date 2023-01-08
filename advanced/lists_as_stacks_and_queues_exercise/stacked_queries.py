number = int(input())

stack = []

for _ in range(number):
    input_line = input().split()
    if len(input_line) == 2:
        stack.append(int(input_line[1]))
    else:
        if input_line[0] == "2":
            if stack:
                stack.pop()
        elif input_line[0] == "3":
            if stack:
                print(max(stack))
        elif input_line[0] == "4":
            if stack:
                print(min(stack))
stack.reverse()
print(", ".join(map(str, stack)))
