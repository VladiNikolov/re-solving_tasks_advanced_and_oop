input_line = [int(i) for i in input().split()]

for element in range(len(input_line)):
    print(input_line.pop(), end=" ")