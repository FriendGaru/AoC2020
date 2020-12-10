def summable(option_numbers, result):
    for i in range(len(option_numbers)):
        for j in range(i + 1, len(option_numbers)):
            if option_numbers[i] + option_numbers[j] == result:
                return True
    return False

working_numbers = []
preamble = 25

with open("input.txt") as file:
    lines = file.read().split('\n')
    current_index = 0
    while current_index < len(lines):
        print(working_numbers)
        next_num = int(lines[current_index])
        if preamble > 0:
            working_numbers.append(next_num)
            preamble -= 1
        elif summable(working_numbers, next_num):
            working_numbers.append(next_num)
            working_numbers.pop(0)
        else:
            print(next_num)
            print(working_numbers)
            break
        current_index += 1


