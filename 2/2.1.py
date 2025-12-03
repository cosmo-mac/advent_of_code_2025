FILE_PATH = 'input.txt'

def is_id_invalid(i):
    i = str(i)
    if len(i) % 2 == 0 and i[:len(i)//2] == i[len(i)//2:]:
        return True
    return False

with open(FILE_PATH) as f:
    invalid_id_sum = 0
    id_ranges = f.read().split(',')
    for id_range in id_ranges:
        lower, higher = id_range.split('-')
        invalid_id_sum += sum(i for i in range(int(lower), int(higher)+1) if is_id_invalid(i))
    print(invalid_id_sum)
