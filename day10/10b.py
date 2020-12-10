with open("input.txt") as file:
    adapter_list = [int(x) for x in file.read().split("\n")]

adapter_list.sort()
adapter_list.insert(0, 0)
adapter_list.append(max(adapter_list) + 3)

print(adapter_list)
adapter_set = set(adapter_list)
adapter_dict = {}

def num_ways_to_destination(adapter_set, destination):
    ways = 0
    for i in [-1, -2, -3]:
        check_adapter = i + destination
        print(check_adapter)
        if check_adapter == 0:
            ways += 1
        elif check_adapter in adapter_dict:
            ways += adapter_dict[check_adapter]
        elif check_adapter in adapter_set:
            ways += num_ways_to_destination(adapter_set, check_adapter)
    adapter_dict[destination] = ways
    return ways


print(num_ways_to_destination(adapter_set, max(adapter_list)))
print(max(adapter_list))