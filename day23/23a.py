test_input = (3, 8, 9, 1, 2, 5, 4, 6, 7)
real_input = (6, 1, 4, 7, 5, 2, 8, 3, 9)

class Cup:
    def __init__(self, label):
        self.label = label
        self.next = None


def build_circle(input_labels):
    cups_dict = {}
    cup_list = []
    lowest_val = 99999999999999
    highest_val = -1
    for label in input_labels:
        lowest_val = min(lowest_val, label)
        highest_val = max(highest_val, label)
        new_cup = Cup(label)
        cups_dict[label] = new_cup
        cup_list.append(new_cup)
    for i in range(len(cup_list) - 1):
        cup_list[i].next = cup_list[i+1]
    cup_list[-1].next = cup_list[0]
    return cup_list[0], cups_dict, lowest_val, highest_val

def labels_from_cup(start_cup:Cup):
    labels = [start_cup.label, ]
    first_cup = start_cup
    while not start_cup.next == first_cup:
        labels.append(start_cup.next.label)
        start_cup = start_cup.next
    return labels

def move(current_cup: Cup, cups_dict: dict, lowest_val, highest_val):
    destination = current_cup.label - 1
    trio_labels = [current_cup.next.label, current_cup.next.next.label, current_cup.next.next.next.label]
    trio_first = cups_dict[trio_labels[0]]
    trio_last = cups_dict[trio_labels[-1]]
    current_cup.next = trio_last.next
    while destination < lowest_val or destination in trio_labels:
        if destination < lowest_val:
            destination = highest_val
            continue
        else:
            destination -= 1
    desination_cup = cups_dict[destination]
    temp_next = desination_cup.next
    desination_cup.next = trio_first
    trio_last.next = temp_next
    next_cup = current_cup.next
    return next_cup




start_cup, cups_dict, lowest_val, highest_val = build_circle(real_input)
print(labels_from_cup(start_cup))

next_cup = start_cup
for i in range(100):
    print(next_cup.label)
    next_cup = move(next_cup, cups_dict, lowest_val, highest_val)
    print(labels_from_cup(next_cup))

one_cup = cups_dict[1]
print("".join([str(x) for x in labels_from_cup(one_cup)[1:]]))


print()
