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
    yes_qs = set()
    for person in group:
        for char in person:
            yes_qs.add(char)
    group_sum = len(yes_qs)
    total_sum += group_sum

print(total_sum)
