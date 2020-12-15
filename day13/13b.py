busses = []
with open("input.txt") as file:
    lines = file.read().split("\n")
    raw_busses = lines[1].split(",")
    for i in range(len(raw_busses)):
        if raw_busses[i].isdigit():
            busses.append((int(raw_busses[i]), i))

period = 1
t = 0

while len(busses) > 0:
    next_bus_period, next_bus_offset = busses.pop()
    while True:
        if (t + next_bus_offset) % next_bus_period == 0:
            period *= next_bus_period
            break
        else:
            t += period

print(t)