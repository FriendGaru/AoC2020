DEFAULT_FACING = 90

class Ship:
    def __init__(self):
        self.facing = DEFAULT_FACING
        self.current_coord = (0, 0)
        self.coord_history = []

    def turn(self, dir, degrees):
        if dir == "L":
            self.facing -= degrees
        elif dir == "R":
            self.facing += degrees
        else:
            raise ValueError
        self.facing = self.facing % 360

    def move_absolute(self, dir, distance):
        self.coord_history.append(self.current_coord)
        if dir == "N":
            vec_x = 0
            vec_y = 1
        elif dir == "E":
            vec_x = 1
            vec_y = 0
        elif dir == "S":
            vec_x = 0
            vec_y = -1
        elif dir == "W":
            vec_x = -1
            vec_y = 0
        else:
            raise ValueError
        vec_x *= distance
        vec_y *= distance
        self.current_coord = (self.current_coord[0] + vec_x, self.current_coord[1] + vec_y)

    def move_forward(self, distance):
        self.coord_history.append(self.current_coord)
        if self.facing == 0:
            vec_x = 0
            vec_y = 1
        elif self.facing == 90:
            vec_x = 1
            vec_y = 0
        elif self.facing == 180:
            vec_x = 0
            vec_y = -1
        elif self.facing == 270:
            vec_x = -1
            vec_y = 0
        else:
            raise ValueError
        vec_x *= distance
        vec_y *= distance
        self.current_coord = (self.current_coord[0] + vec_x, self.current_coord[1] + vec_y)

ship = Ship()
with open("input.txt") as file:
    for line in file:
        line = line.strip()
        instruction = line[0]
        val = int(line[1:])

        if instruction in ("L", "R"):
            ship.turn(instruction, val)
        elif instruction in ("N", "E", "S", "W"):
            ship.move_absolute(instruction, val)
        elif instruction == "F":
            ship.move_forward(val)
        else:
            raise ValueError

print(ship.coord_history)
print(ship.current_coord)
print(abs(ship.current_coord[0]) + abs(ship.current_coord[1]))


