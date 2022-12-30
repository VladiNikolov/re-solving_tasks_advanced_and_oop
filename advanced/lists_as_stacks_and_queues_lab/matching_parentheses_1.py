input_line = input()

stack = []
for index in range(len(input_line)):
    current_element = input_line[index]

    if current_element == "(":
        stack.append(index)
    elif current_element == ")":
        last_opening_bracket = stack.pop()
        result = input_line[last_opening_bracket:index + 1]
        print(result)

        