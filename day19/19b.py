import itertools

# Takes an iterable like ((1, 2, 3), (4, 5))
# Returns a list of permutations, respecting variable order
# ((1, 2, 3), (4, 5))) -> [[1, 4], [1, 5], [2, 4], [2, 5], [3, 4], [3, 5]]
def positional_permutatons(thing):
    if len(thing) == 1:
        perms = []
        for x in thing[0]:
            new_list = [x]
            perms.append(new_list)
        return perms
    else:
        next_part = thing[0]
        perms = []
        for item in next_part:
            for sub_perm in positional_permutatons(thing[1:]):
                sub_perm.insert(0, item)
                perms.append(sub_perm)
        return perms

rules = {}
messages = []

def build_rules_messages(filename):
    with open(filename) as file:
        lines = file.read().split("\n")
        while lines:
            line = lines.pop(0)
            if line == '':
                break
            rule_num, rule_parts = line.split(":")
            rule_parts = rule_parts.strip()
            if '"' in rule_parts:
                rule_parts = rule_parts.replace('"', "")
                rules[rule_num] = rule_parts.strip()
            else:
                sub_rules = rule_parts.split("|")
                sub_rule_tups = []
                for sub_rule in sub_rules:
                    sub_rule = sub_rule.strip()
                    sub_rule_tup = list(sub_rule.split(" "))
                    sub_rule_tups.append(sub_rule_tup)
                rules[rule_num] = sub_rule_tups


        while lines:
            line = lines.pop(0)
            messages.append(line)

# Update rules
def update_rules():
    rules["8"] = [["42"], ["42", "8"]]
    rules["11"] = [["42", "31"], ["42", "11", "31"]]

def remove_prefix(text, prefix):
    return text[text.startswith(prefix) and len(prefix):]

# Takes a list of rules, returns True if it matches, False if it doesn't
def match_rules(rule_id_list, remaining_message):
    if len(rule_id_list) > len(remaining_message):
        return False
    assert isinstance(remaining_message, str)
    next_rule_id = rule_id_list[0]
    next_rule_content = rules[next_rule_id]
    # If the next rule to check is a string, it's potentially terminating
    if isinstance(next_rule_content, str):
        match_text = rules[next_rule_id]
        if remaining_message.startswith(match_text):
            new_remaining_message = remove_prefix(remaining_message, match_text)
            if len(new_remaining_message) == 0 and len(rule_id_list) == 1:
                return True
            elif len(new_remaining_message) == 0:
                return False
            elif len(rule_id_list) == 1:
                return False
            else:
                return match_rules(rule_id_list[1:], new_remaining_message)
        else:
            return False
    else:
        permutations = []
        for sub_pattern in next_rule_content:
            permutations.append(sub_pattern + rule_id_list[1:])
        for permutation in permutations:
            if match_rules(permutation, remaining_message):
                return True
        return False


build_rules_messages("input.txt")
update_rules()

count = 0
for message in messages:
    match_found = match_rules(["0",], message)
    if match_found:
        count += 1
    print("Message: " + message)
    print("Match: " + str(match_found))

print("Count: " + str(count))


# 383 is too high



