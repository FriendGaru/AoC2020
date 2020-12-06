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

input = "input.txt"
passport = {}
valid_count = 0
total_passports = 0
with open(input) as file:
    for line in file:
        if line.strip() == "":
            passport_valid = True
            for required_field in required_fields:
                if required_field not in passport:
                    passport_valid = False
                    break
            if passport_valid:
                valid_count += 1
            total_passports += 1
            passport = {}
        else:
            chunks = line.strip().split(" ")
            for chunk in chunks:
                k, v = chunk.split(":")
                passport[k] = v

print(valid_count)
print(total_passports)

