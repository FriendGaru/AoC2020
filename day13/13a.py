with open("input.txt") as file:
    lines = file.read().split("\n")
    time = int(lines[0].strip())
    busses = lines[1].strip().split(",")

valid_busses = []
for bus in busses:
    if bus == "x":
        continue
    else:
        valid_busses.append(int(bus))

def bus_check(bus_id):
    return ((time // bus_id) + 1) * bus_id

best_wait = 99999999999999999
best_bus = 0
for bus in valid_busses:
    check = bus_check(bus)
    if check < best_wait:
        best_wait = check
        best_bus = bus

print(best_bus, best_wait, (best_wait-time)*best_bus)