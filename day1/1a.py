input = []
with open("input.txt") as file:
    for line in file:
        input.append(int(line.strip()))

input.sort()
for i in range(len(input)):
    for j in range(i+1, len(input)):
        if input[i] + input[j] == 2020:
            print(input[i])
            print(input[j])
            print(input[i] * input[j])