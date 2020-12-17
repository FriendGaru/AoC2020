def add_coords(x1, y1, z1, x2, y2, z2):
    return (x1 + x2, y1 + y2, z1 + z2)

def get_coord_neighbors(x, y, z):
    neighbors = []
    for _z in (-1, 0, 1):
        for _y in (-1, 0, 1):
            for _x in (-1, 0, 1):
                if _x == 0 and _y == 0 and _z == 0:
                    continue
                neighbors.append(add_coords(x, y, z, _x, _y, _z))
    return neighbors


class Pocket_Dimension:
    def __init__(self):
        self.active_coords = set()
        self.current_iteration = 0

    def init(self, filename):
        with open(filename) as file:
            lines = file.readlines()
            for y in range(len(lines)):
                line = lines[y].strip()
                for x in range(len(line)):
                    if lines[y][x] == "#":
                        self.active_coords.add((x, y, 0))

    def iterate(self):
        possible_active_coords = {}
        for active_coord in self.active_coords:
            for neighbor in get_coord_neighbors(*active_coord):
                if neighbor in possible_active_coords:
                    possible_active_coords[neighbor] += 1
                else:
                    possible_active_coords[neighbor] = 1

        new_active_coords = set()
        for check_coord in possible_active_coords.keys():
            if check_coord in self.active_coords \
             and possible_active_coords[check_coord] in (2, 3):
                new_active_coords.add(check_coord)
            elif check_coord not in self.active_coords \
             and possible_active_coords[check_coord] == 3:
                new_active_coords.add(check_coord)

        self.active_coords = new_active_coords
        self.current_iteration += 1

    def display(self):
        print("Current Iteration: " + str(self.current_iteration))
        min_x = min([xyz[0] for xyz in self.active_coords])
        max_x = max([xyz[0] for xyz in self.active_coords])
        min_y = min([xyz[1] for xyz in self.active_coords])
        max_y = max([xyz[1] for xyz in self.active_coords])
        min_z = min([xyz[2] for xyz in self.active_coords])
        max_z = max([xyz[2] for xyz in self.active_coords])

        for z in range(min_z, max_z+1):
            print("Z: " + str(z))
            for y in range(min_y, max_y+1):
                line = ""
                for x in range(min_x, max_x+1):
                    if (x, y, z) in self.active_coords:
                        line += "#"
                    else:
                        line += "."
                print(line)
            print()

    def disp_count(self):
        print("Active Coordinates: " + str(len(pd.active_coords)))
        print()

pd = Pocket_Dimension()
pd.init("input.txt")
pd.display()
pd.disp_count()
pass
for i in range(6):
    pd.iterate()
    pd.display()
    pd.disp_count()
    pass