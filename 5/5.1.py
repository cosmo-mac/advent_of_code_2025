"""
Yes there are more nuanced approaches, it was 8:30 in the morning
"""

def isFruitInRange(fruit_id, id_range):
    lower, higher = map(int, id_range.split('-'))
    fruit_id = int(fruit_id)
    if fruit_id >= lower and fruit_id <= higher:
        return True
    return False

def countFreshFruit(fruit_ids, id_ranges):
    count = 0
    for fruit_id in fruit_ids:
        for id_range in id_ranges:
            if isFruitInRange(fruit_id, id_range):
                count += 1
                break
    return count

FILE_PATH = "input.txt"

with open(FILE_PATH) as f:
    id_ranges = []
    fruit_ids = []
    while (line := f.readline().strip()) != "":
        id_ranges.append(line)
    while line := f.readline().strip():
        fruit_ids.append(line)
    print(countFreshFruit(fruit_ids, id_ranges))