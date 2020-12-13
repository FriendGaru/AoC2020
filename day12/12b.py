class Ship:
    def __init__(self):
        self.waypoint_x = 10
        self.waypoint_y = 1
        self.current_x = 0
        self.current_y = 0
        self.coord_history = []

    def display(self):
        print("Current Coords: {}, {}   Current Waypoint: {}, {}".format(self.current_x, self.current_y,
                                                                         self.waypoint_x, self.waypoint_y))

    def turn(self, dir, degrees):
        if dir == "L":
            while degrees > 0:
                degrees -= 90
                self.waypoint_x, self.waypoint_y = -self.waypoint_y, self.waypoint_x
        elif dir == "R":
            while degrees > 0:
                degrees -= 90
                self.waypoint_x, self.waypoint_y = self.waypoint_y, -self.waypoint_x
        else:
            raise ValueError

    def move_waypoint(self, dir, distance):
        self.coord_history.append((self.current_x, self.current_y))
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
        self.waypoint_x += vec_x
        self.waypoint_y += vec_y

    def move_forward(self, distance):
        self.coord_history.append((self.current_x, self.current_y))

        self.current_x += self.waypoint_x * distance
        self.current_y += self.waypoint_y * distance

ship = Ship()
with open("input.txt") as file:
    for line in file:
        line = line.strip()
        instruction = line[0]
        val = int(line[1:])

        ship.display()
        if instruction in ("L", "R"):
            ship.turn(instruction, val)
        elif instruction in ("N", "E", "S", "W"):
            ship.move_waypoint(instruction, val)
        elif instruction == "F":
            ship.move_forward(val)
        else:
            raise ValueError

ship.display()
print(ship.coord_history)
print(ship.current_x, ship.current_y)
print(abs(ship.current_x) + abs(ship.current_y))


