input_line = list(input())

bracket_list = []
for index in range(len(input_line)):
    if input_line[index] == "(":
        bracket_list.append(index)
    elif input_line[index] == ")":
        last_opening_bracket = bracket_list.pop()
        sub_string = input_line[last_opening_bracket:index + 1]
        print(''.join(sub_string))
