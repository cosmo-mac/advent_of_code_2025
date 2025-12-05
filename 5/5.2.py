"""
Deepcopying lists never feels like a super duper good idea but oh well
Demonstrates an even further lack of nuance, better approach would be to first sort
id ranges indexed by lower bound then upper bound, then restructuring id range
would only require one pass through. But a solution is a solution :P
"""

import copy

def new_ranges(id_ranges):
    new_range = [id_ranges.pop(0)]
    while len(id_ranges) > 0:
        lower, higher = id_ranges.pop(0)
        redundant = False
        new_range_copy = copy.deepcopy(new_range)
        for check_range in new_range:
            check_lower, check_higher = check_range
            if lower <= check_lower and higher >= check_higher:
                new_range_copy.remove(check_range)
            elif lower <= check_higher and lower >= check_lower and higher >= check_higher:
                lower = check_higher + 1
            elif higher >= check_lower and higher <= check_higher and lower <= check_lower:
                higher = check_lower - 1
            elif lower >= check_lower and higher <= check_higher:
                redundant = True
                break
        if not redundant:
            new_range_copy.append((lower, higher))
        new_range = new_range_copy
    return new_range

def possible_fresh(id_ranges):
    new_range = new_ranges(id_ranges)
    count = 0
    for low, high in new_range:
        count += high - low + 1
    return count

FILE_PATH = "input.txt"

with open(FILE_PATH) as f:
    id_ranges = []
    while (line := f.readline().strip()) != "":
        id_range = tuple(map(int, line.split('-')))
        id_ranges.append(id_range)

    print(possible_fresh(id_ranges))