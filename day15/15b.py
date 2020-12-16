import time
timer = time.perf_counter()
input = [18, 8, 0, 5, 4, 1, 20]
# input = [0, 3, 6]
# input = [1,3,2]



current_turn = 1
target_turn = 30000000
numbers_used = {}
last_number = None
skip_first = True

while current_turn <= target_turn:
    if input:
        last_number = input.pop(0)
        numbers_used[last_number] = current_turn
    elif skip_first:
        last_number = 0
        skip_first = False
    elif last_number in numbers_used:
        next_number = current_turn - numbers_used[last_number] - 1
        numbers_used[last_number] = current_turn -1
        last_number = next_number
    else:
        numbers_used[last_number] = current_turn -1
        last_number = 0
    # print(last_number)
    if current_turn % 100000 == 0:
        print("turn: "+ str(current_turn))
    current_turn += 1
print(last_number)
print(str(time.perf_counter() - timer))


