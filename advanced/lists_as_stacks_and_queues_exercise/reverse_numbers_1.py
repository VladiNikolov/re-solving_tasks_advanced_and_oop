input_line = input().split()

integer_list = []
for el in input_line:
    integer_list.append(int(el))

integer_list.reverse()
print(" ".join(map(str, integer_list)))