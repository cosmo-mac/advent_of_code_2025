"""
    Decided to actually make nice
    O(nlogn) time due to initial sort
    and O(1) space!
"""

def possible_fresh(id_ranges):
    id_ranges.sort(key = lambda id_range : (id_range[0], id_range[1]))
    new_range = id_ranges[0]
    count = new_range[1] - new_range[0] + 1
    for i in range(1, len(id_ranges)):
        lower, higher = id_ranges[i]
        check_lower, check_higher = new_range
        if higher <= check_higher:
            continue
        elif lower <= check_higher and higher >= check_higher:
            new_range = (check_higher + 1, higher)
            count += higher - check_higher
        elif lower > check_higher:
            new_range = (lower, higher)
            count += higher - lower + 1
    return count

FILE_PATH = "test.txt"

with open(FILE_PATH) as f:
    id_ranges = []
    while (line := f.readline().strip()) != "":
        id_range = tuple(map(int, line.split('-')))
        id_ranges.append(id_range)
    print(possible_fresh(id_ranges))