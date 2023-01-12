input_line = [int(i) for i in input().split()]

for index in range(len(input_line) - 1, -1, -1):
    current_number = input_line[index]
    print(current_number, end=" ")