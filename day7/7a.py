def parse_bag(bag_string):
    bag_string = bag_string.strip()
    bag_string = bag_string.replace("contains", "contain")
    bag_string = bag_string.replace("bags", "bag")
    bag_string = bag_string.replace(".", "")
    out_bag, inner_bag_chunk = bag_string.split("contain")
    out_bag = out_bag.replace("bag", "")
    out_bag = out_bag.strip()
    inner_bags_raw = inner_bag_chunk.split(",")
    inner_bags = []
    for inner_bag in inner_bags_raw:
        inner_bag = inner_bag.strip()
        if inner_bag == "no other bag":
            continue
        num_bags = inner_bag[0:2]
        num_bags = int(num_bags)
        inner_bag = inner_bag.replace("bag", "")
        inner_bags.append((num_bags, inner_bag[2:].strip()))
    return out_bag, inner_bags

is_contained_by = {}
with open("input.txt") as file:
    for line in file:
        out_bag, inner_bags = parse_bag(line)
        for num, bag in inner_bags:
            if num <= 0:
                continue
            else:
                if bag not in is_contained_by:
                    is_contained_by[bag] = set()
                is_contained_by[bag].add(out_bag)

checked_bags = set()
unchecked_bags = set()

unchecked_bags.add("shiny gold")

while len(unchecked_bags) > 0:
    next_check = unchecked_bags.pop()
    if next_check in checked_bags:
        continue
    checked_bags.add(next_check)
    if next_check in is_contained_by:
        unchecked_bags.update(is_contained_by[next_check])
        pass

# Minus one so we don't count the bag itself
print(len(checked_bags) -1)





