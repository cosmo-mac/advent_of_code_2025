FILE_PATH = 'input.txt'

with open(FILE_PATH) as f:
    curr_position = 50
    counter = 0

    while True:
        line = f.readline().strip()
        if not line:
            break

        direction, length = line[0], line[1:]
        if direction == "L":
            curr_position = (curr_position - int(length)) % 100
        if direction == "R":
            curr_position = (curr_position + int(length)) % 100

        if curr_position == 0:
            counter += 1

        print(curr_position)
    print(f'counter: {counter}')