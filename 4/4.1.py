import copy

DIRS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 1),
    (1, -1), (1, 0), (1, 1)
]

def is_roll_accessible(rolls, y, x):
    count = 0
    for dy, dx in DIRS:
        test_pos_y, test_pos_x = y + dy, x + dx
        if test_pos_y >= 0 and test_pos_y < len(rolls) and test_pos_x >= 0 and test_pos_x < len(rolls[0]):
            if rolls[test_pos_y][test_pos_x] == '@':
                count += 1
        if count >= 4:
            return False
    return True

def count_rolls(rolls):
    count = 0
    for y in range(len(rolls)):
        for x in range(len(rolls[0])):
            if rolls[y][x] == '@' and is_roll_accessible(rolls, y, x):
                count += 1
    return count

FILE_PATH = 'input.txt'

with open(FILE_PATH) as f:
    rolls = [[char for char in row.strip()] for row in f.readlines()]
    print(count_rolls(rolls))