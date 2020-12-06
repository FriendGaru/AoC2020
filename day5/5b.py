import math

boarding_passes = []
with open("input.txt") as file:
    for line in file:
        if line == "":
            break
        else:
            boarding_passes.append(line.strip())

def check_pass(boarding_pass):
    assert len(boarding_pass) == 10
    row_min = 0
    row_max = 127
    for row_char in boarding_pass[0:7]:
        if row_char == "F":
            row_max = math.floor((row_min + row_max) / 2)
        elif row_char == "B":
            row_min = math.ceil((row_min + row_max) / 2)
        else:
            raise ValueError
    assert row_min == row_max
    row = row_min
    col_min = 0
    col_max = 7
    for col_char in boarding_pass[7:10]:
        if col_char == "L":
            col_max = math.floor((col_min + col_max) / 2)
        elif col_char == "R":
            col_min = math.ceil((col_min + col_max) / 2)
        else:
            raise ValueError
    assert col_min == col_max
    col = col_min
    return row, col

def seat_id(row, col):
    return row*8+col

filled_seats = set()
for boarding_pass in boarding_passes:
    row, col = check_pass(boarding_pass)
    filled_seats.add(seat_id(row, col))

for r in range(128):
    for c in range(8):
        id = seat_id(r, c)
        if id not in filled_seats and id + 1 in filled_seats and id -1 in filled_seats:
            print(r, c, id)

