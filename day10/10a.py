with open("input.txt") as file:
    adapter_list = [int(x) for x in file.read().split("\n")]

adapter_list.sort()
adapter_list.insert(0, 0)
adapter_list.append(max(adapter_list) + 3)

print(adapter_list)
one_jumps = 0
three_jumps = 0
for i in range(len(adapter_list) - 1):
    if adapter_list[i+1] - adapter_list[i] == 1:
        one_jumps += 1
    elif adapter_list[i+1] - adapter_list[i] == 3:
        three_jumps += 1

print("One jumps: " + str(one_jumps))
print("Three jumps: " + str(three_jumps))
print("Result: " + str(one_jumps * three_jumps))
