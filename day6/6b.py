groups = []
with open("input.txt") as file:
    new_group = []
    for line in file:
        line = line.strip()
        if line == "":
            groups.append(new_group)
            new_group = []
        else:
            new_group.append(line)


total_sum = 0
for group in groups:
    group_size = len(group)
    yes_qs = {}
    for person in group:
        for char in person:
            if char in yes_qs:
                yes_qs[char] += 1
            else:
                yes_qs[char] = 1
    group_sum = 0
    for val in yes_qs.values():
        if val == group_size:
            group_sum += 1
    total_sum += group_sum

print(total_sum)
