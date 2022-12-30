from collections import deque

input_line = input()
people_deque = deque()

while input_line != "End":

    if input_line == "Paid":
        print('\n'.join(people_deque))
        people_deque.clear()
    else:
        people_deque.append(input_line)

    input_line = input()

print(f"{len(people_deque)} people remaining.")