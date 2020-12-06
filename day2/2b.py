class Password:
    def __init__(self, policy_letter, letter_min, letter_max, password):
        self.policy_letter = policy_letter
        self.letter_min = int(letter_min)
        self.letter_max = int(letter_max)
        self.password = password.strip()

    def verify(self):
        count = 0
        if self.password[self.letter_min - 1] == self.policy_letter:
            count += 1
        if self.password[self.letter_max - 1] == self.policy_letter:
            count += 1
        if count == 1:
            return True
        else:
            return False

passwords = []

with open("input.txt") as file:
    for line in file:
        policy_chunk, password_chunk = line.split(":")
        min_max, letter = policy_chunk.split(" ")
        min, max = min_max.split("-")
        new_pass = Password(letter.strip(), int(min), int(max), password_chunk.strip())
        passwords.append(new_pass)

count = 0
for password in passwords:
    if password.verify():
        count+=1

print(count)