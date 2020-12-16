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

valid_tickets = []
for ticket in tickets:
    ticket_valid = True
    for field_val in ticket:
        field_match_found = False
        for category, cat_ranges in categories_and_ranges.items():
            if field_match_found:
                break
            for cat_range in cat_ranges:
                if field_val in cat_range:
                    field_match_found = True
        if not field_match_found:
            ticket_valid = False
            break
    if ticket_valid:
        valid_tickets.append(ticket)
print("All Tickets")
print(tickets)
print("Valid Tickets")
print(valid_tickets)

print("Categories and ranges")
print(categories_and_ranges)

def valid_categories_for_value(val):
    valid_cats = set()
    for cat in categories_and_ranges.keys():
        for cat_range in categories_and_ranges[cat]:
            if val in cat_range:
                valid_cats.add(cat)
                break
    return valid_cats

possible_field_cats = [set(categories_and_ranges.keys()) for _ in range(len(categories_and_ranges.keys()))]
for field_index in range(len(possible_field_cats)):
    for ticket in valid_tickets:
        check_val = ticket[field_index]
        possible_cats_for_val = valid_categories_for_value(check_val)
        possible_field_cats[field_index] = possible_field_cats[field_index].intersection(possible_cats_for_val)

known_cats = [None for _ in range(len(categories_and_ranges.keys()))]

found_check = True
while found_check:
    found_check = False
    for i in range(len(possible_field_cats)):
        if len(possible_field_cats[i]) == 1:
            found_check = True
            certain_cat = possible_field_cats[i].pop()
            known_cats[i] = certain_cat
            for i in range(len(possible_field_cats)):
                if certain_cat in possible_field_cats[i]:
                    possible_field_cats[i].remove(certain_cat)

print(known_cats)

total = 1
for i in range(len(known_cats)):
    assert isinstance(known_cats[i], str)
    if known_cats[i].startswith("dep"):
        print(known_cats[i])
        print(my_ticket[i])
        total *= my_ticket[i]

print("Total")
print(total)




