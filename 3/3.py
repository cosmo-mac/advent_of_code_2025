def joltage(bank, starting_index, length):
    if length == 0:
        return ''
    max_digit_index = starting_index
    for i in range(starting_index, len(bank) - length + 1):
        if bank[i] > bank[max_digit_index]:
            max_digit_index = i
    return bank[max_digit_index] + joltage(bank, max_digit_index + 1, length - 1)

FILE_PATH = 'input.txt'

# part 1
with open(FILE_PATH) as f:
    print(sum(int(joltage(bank.strip(), 0, 2)) for bank in f.readlines()))

# part 2
with open(FILE_PATH) as f:
    print(sum(int(joltage(bank.strip(), 0, 12)) for bank in f.readlines()))