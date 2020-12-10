def summable(option_numbers, result):
    for i in range(len(option_numbers)):
        for j in range(i + 1, len(option_numbers)):
            if option_numbers[i] + option_numbers[j] == result:
                return True
    return False


working_numbers = []
preamble = 25

with open("input.txt") as file:
    numbers = [int(x) for x in file.read().split('\n')]

current_index = 0
target_sum = -1
while current_index < len(numbers):
    next_num = int(numbers[current_index])
    if preamble > 0:
        working_numbers.append(next_num)
        preamble -= 1
    elif summable(working_numbers, next_num):
        working_numbers.append(next_num)
        working_numbers.pop(0)
    else:
        print(next_num)
        print(working_numbers)
        target_sum = next_num
        break
    current_index += 1

contiguous_len = 2
contiguous_group = None
while contiguous_len <= len(numbers) and not contiguous_group:
    print("Checking length " + str(contiguous_len))
    next_index = 0
    while next_index + contiguous_len <= len(numbers):
        test_sum = sum(numbers[next_index: next_index + contiguous_len])
        if test_sum == target_sum:
            print(numbers[next_index: next_index + contiguous_len])
            contiguous_group = numbers[next_index: next_index + contiguous_len]
            break
        next_index += 1
    contiguous_len += 1

encryption_weakness = min(contiguous_group) + max(contiguous_group)
print("Encryption Weakness")
print(encryption_weakness)
