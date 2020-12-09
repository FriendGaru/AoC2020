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

bag_contains = {}
with open("input.txt") as file:
    for line in file:
        out_bag, inner_bags = parse_bag(line)
        bag_contains[out_bag] = []
        for num, bag in inner_bags:
            if num <= 0:
                continue
            else:
                bag_contains[out_bag].append((num, bag))


def how_many_bags_to_fill(bag):
    if len(bag_contains[bag]) == 0:
        return 0
    else:
        total = 0
        for num, inner_bag in bag_contains[bag]:
            total += num
            total += num * how_many_bags_to_fill(inner_bag)
        return total

print(how_many_bags_to_fill('shiny gold'))






