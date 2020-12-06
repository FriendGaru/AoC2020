required_fields = (
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
    # "cid",
)

def check_byr(input):
    input = str(input)
    if len(input) == 4 and input.isdigit() and 1920 <= int(input) <= 2002:
        return True
    else:
        return False

def check_iyr(input):
    input = str(input)
    if len(input) == 4 and input.isdigit() and 2010 <= int(input) <= 2020:
        return True
    else:
        return False

def check_eyr(input):
    input = str(input)
    if len(input) == 4 and input.isdigit() and 2020 <= int(input) <= 2030:
        return True
    else:
        return False

def check_hgt(input):
    input = str(input)
    if input[-2:] == 'in':
        if input[0:-2].isdigit() and 59 <= int(input[0:-2]) <= 76:
            return True
        else:
            return False
    elif input[-2:] == 'cm':
        if input[0:-2].isdigit() and 150 <= int(input[0:-2]) <= 193:
            return True
        else:
            return False
    else:
        return False

def check_hcl(input):
    if not input[0] == "#":
        return False
    for char in input[1:]:
        if char not in {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'}:
            return False
    return True

def check_ecl(input):
    if input in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
        return True
    return False

def check_pid(input):
    if input.isdigit() and len(input) == 9:
        return True
    return False

input = "input.txt"
passport = {}
valid_count = 0
total_passports = 0
with open(input) as file:
    for line in file:
        if line.strip() == "":
            passport_valid = True
            if 'byr' not in passport or not check_byr(passport['byr']):
                passport_valid = False
            if 'ecl' not in passport or not check_ecl(passport['ecl']):
                passport_valid = False
            if 'eyr' not in passport or not check_eyr(passport['eyr']):
                passport_valid = False
            if 'hcl' not in passport or not check_hcl(passport['hcl']):
                passport_valid = False
            if 'hgt' not in passport or not check_hgt(passport['hgt']):
                passport_valid = False
            if 'iyr' not in passport or not check_iyr(passport['iyr']):
                passport_valid = False
            if 'pid' not in passport or not check_pid(passport['pid']):
                passport_valid = False
            if passport_valid:
                valid_count += 1
                print("VALID")
                for field in required_fields:
                    print(field + ": " + passport[field])
            total_passports += 1

            passport = {}
        else:
            chunks = line.strip().split(" ")
            for chunk in chunks:
                k, v = chunk.split(":")
                passport[k] = v

print(valid_count)
print(total_passports)

