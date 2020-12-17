def add_coords(x1, y1, z1, w1, x2, y2, z2, w2):
    return x1 + x2, y1 + y2, z1 + z2, w1 + w2


def get_coord_neighbors(x, y, z, w):
    neighbors = []
    for _w in (-1, 0, 1):
        for _z in (-1, 0, 1):
            for _y in (-1, 0, 1):
                for _x in (-1, 0, 1):
                    if _x == 0 and _y == 0 and _z == 0 and _w == 0:
                        continue
                    neighbors.append(add_coords(x, y, z, w, _x, _y, _z, _w))
    return neighbors


class PocketDimension:
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
                        self.active_coords.add((x, y, 0, 0))

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

    def disp_count(self):
        print("Current Iteration: " + str(self.current_iteration))
        print("Active Coordinates: " + str(len(pd.active_coords)))
        print()


pd = PocketDimension()
pd.init("input.txt")
pd.disp_count()

for i in range(6):
    pd.iterate()
    pd.disp_count()