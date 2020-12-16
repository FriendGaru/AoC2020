categories_and_ranges = {}
my_ticket = None
tickets = []

with open("input.txt") as file:
    lines = file.read().split("\n")
    # Categories
    while lines:
        line = lines.pop(0)
        if line == "":
            break
        else:
            category, cat_ranges = line.split(":")
            cat_ranges = cat_ranges.split("or")
            clean_ranges = []
            for cat_range in cat_ranges:
                min, max = cat_range.split("-")
                min = int(min)
                max = int(max)
                clean_ranges.append(range(min, max+1))
            categories_and_ranges[category.strip()] = clean_ranges
    # My Ticket
    lines.pop(0)
    my_ticket = [int(x) for x in lines.pop(0).split(",")]

    # Other Tickets
    lines.pop(0)
    lines.pop(0)
    while(lines):
        tickets.append([int(x) for x in lines.pop(0).split(",")])

error_vals = []
for ticket in tickets:
    for field_val in ticket:
        field_match_found = False
        for category, cat_ranges in categories_and_ranges.items():
            if field_match_found:
                break
            for cat_range in cat_ranges:
                if field_val in cat_range:
                    field_match_found = True
        if not field_match_found:
            error_vals.append(field_val)

print(error_vals)
print(sum(error_vals))


