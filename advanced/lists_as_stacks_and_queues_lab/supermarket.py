from collections import deque

people_deque = deque()

while True:
    input_line = input()
    if input_line == "End":
        break

    if input_line == "Paid":
        print("\n".join(people_deque))
        people_deque.clear()
    else:
        people_deque.append(input_line)

print(f"{len(people_deque)} people remaining.")