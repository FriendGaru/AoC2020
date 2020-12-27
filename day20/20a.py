def compare_2d_arrays(array1, array2):
    try:
        assert len(array1) == len(array2)
        for i in range(len(array1)):
            for j in range(len(array1[i])):
                if not array1[i][j] == array2[i][j]:
                    return False
        return True
    except (ValueError, AssertionError):
        return False

class Tile:
    def __init__(self, tile_id):
        self.tile_id = tile_id
        self.original_rows = []
        self.permutations = []
        self.possible_borders = set()
        self.size = None

    def finalize(self):
        self.size = len(self.original_rows)
        for row in self.original_rows:
            assert self.size == len(row)
        self.original_rows = tuple(row for row in self.original_rows)

        self.build_possible_borders()
        self.build_permutations()

    def build_possible_borders(self):
        top = self.original_rows[0]
        self.possible_borders.add(top)
        self.possible_borders.add("".join(reversed(top)))
        bottom = self.original_rows[-1]
        self.possible_borders.add(bottom)
        self.possible_borders.add("".join(reversed(bottom)))
        left = "".join([row[0] for row in self.original_rows])
        self.possible_borders.add(left)
        self.possible_borders.add("".join(reversed(left)))
        right = "".join([row[-1] for row in self.original_rows])
        self.possible_borders.add(right)
        self.possible_borders.add("".join(reversed(right)))

    def build_permutations(self):

        for i in range(2):
            permutation_rows = [row for row in self.original_rows]
            for j in range(i):
                temp_rows = []
                for r in range(10):
                    temp_rows.append("".join([row[r] for row in reversed(permutation_rows)]))
                permutation_rows = temp_rows
            self.permutations.append(tuple([row for row in permutation_rows]))
            self.permutations.append(tuple(reversed([row for row in permutation_rows])))
            self.permutations.append(tuple(["".join(reversed(row)) for row in permutation_rows]))
            self.permutations.append(tuple(reversed(tuple(["".join(reversed(row)) for row in permutation_rows]))))

    def check_dupes(self):
        for i in range(len(self.permutations)):
            for j in range(len(self.permutations)):
                if i == j:
                    continue
                if compare_2d_arrays(self.permutations[i], self.permutations[j]):
                    print("Permutation same: " + str(i) + "  " + str(j))

    def top_border(self, permutation):
        return self.permutations[permutation][0]

    def right_border(self, permutation):
        return "".join([row[-1] for row in self.permutations[permutation]])

    def bottom_border(self, permutation):
        return self.permutations[permutation][-1]

    def left_border(self, permutation):
        return "".join([row[0] for row in self.permutations[permutation]])

    def get_borders(self, permutation):
        return self.top_border(permutation), self.right_border(permutation), \
               self.bottom_border(permutation), self.left_border(permutation)

    def display(self, permutation):
        print("Tile ID: {}  Permutation: {}".format(str(self.tile_id), str(permutation)))
        for row in self.permutations[permutation]:
            print(row)
        print("")

    def display_all(self):
        for i in range(len(self.permutations)):
            self.display(i)


def build_tiles_from_file(filename):
    all_tiles = {}
    with open(filename) as file:
        new_tile = None
        for line in file:
            line = line.strip()
            if line.startswith("Tile"):
                line = line.replace("Tile ", "")
                line = line.replace(":", "")
                tile_id = int(line)
                new_tile = Tile(tile_id)
            elif line == "":
                assert new_tile
                all_tiles[new_tile.tile_id] = new_tile
                new_tile = None
            else:
                assert new_tile
                new_tile.original_rows.append(line)
        if new_tile:
            all_tiles[new_tile.tile_id] = new_tile
    for tile in all_tiles.values():
        assert isinstance(tile, Tile)
        tile.finalize()
    return all_tiles


def build_neighbor_count_dict(all_tiles_dict: dict):
    tile_possible_neighbors = {}
    for tile_id, tile in all_tiles_dict.items():
        tile_possible_neighbors[tile_id] = 0
        assert (isinstance(tile, Tile))
        for other_tile_id, other_tile in all_tiles_dict.items():
            if tile_id == other_tile_id:
                continue
            else:
                assert isinstance(other_tile, Tile)
                if not tile.possible_borders.isdisjoint(other_tile.possible_borders):
                    tile_possible_neighbors[tile_id] += 1
    return tile_possible_neighbors

def sort_tiles(tile_possible_neighbors_dict: dict):
    corner_tiles = []
    border_tiles = []
    inner_tiles = []
    for tile_id, neighbors in tile_possible_neighbors_dict.items():
        if neighbors < 2:
            raise ValueError("Tile with less than two possible neighbors!")
        elif neighbors == 2:
            corner_tiles.append(tile_id)
        elif neighbors == 3:
            border_tiles.append(tile_id)
        else:
            inner_tiles.append(tile_id)
    return corner_tiles, border_tiles, inner_tiles


def determine_board_size(all_tiles: dict):
    size = len(all_tiles.keys()) ** (1 / 2)
    assert int(size) * int(size) == len(all_tiles.keys())
    return int(size)


class Board:
    def __init__(self, board_size, placed_tiles: dict = None):
        self.board_size = board_size
        if placed_tiles:
            self.placed_tiles = placed_tiles.copy()
        else:
            self.placed_tiles = {}
        self.unused_tile_ids = None

    def update_unused_tile_ids(self):
        self.unused_tile_ids = set(all_tiles.keys())
        for tile_id, perm in self.placed_tiles.values():
            self.unused_tile_ids.remove(tile_id)


    def coord_is_corner(self, row, col):
        if row in (0, self.board_size - 1) and col in (0, self.board_size - 1):
            return True

    def coord_is_border(self, row, col):
        if row in (0, self.board_size - 1) or col in (0, self.board_size - 1):
            return True

    # Takes a coordinate, tile id, and permutation and returns a new board state with the tile placed
    def place_tile(self, row, col, tile_id, permutation):
        assert tile_id in all_tiles
        assert (row, col) not in self.placed_tiles
        assert tile_id in self.unused_tile_ids
        new_board = Board(self.board_size, self.placed_tiles)
        new_board.placed_tiles[(row, col)] = (tile_id, permutation)
        new_board.update_unused_tile_ids()
        return new_board

    def get_coord_borders(self, row, col):
        top = None
        if (row -1, col) in self.placed_tiles:
            neighbor_tile_id, permutation = self.placed_tiles[(row -1, col)]
            top = all_tiles[neighbor_tile_id].bottom_border(permutation)

        right = None
        if (row, col + 1) in self.placed_tiles:
            neighbor_tile_id, permutation = self.placed_tiles[(row, col + 1)]
            right = all_tiles[neighbor_tile_id].left_border(permutation)

        bottom = None
        if (row + 1, col) in self.placed_tiles:
            neighbor_tile_id, permutation = self.placed_tiles[(row + 1, col)]
            bottom = all_tiles[neighbor_tile_id].top_border(permutation)

        left = None
        if (row, col - 1) in self.placed_tiles:
            neighbor_tile_id, permutation = self.placed_tiles[(row, col - 1)]
            left = all_tiles[neighbor_tile_id].right_border(permutation)

        return top, right, bottom, left

    def can_place_tile(self, row, col, tile_id, permutation):
        tile = all_tiles[tile_id]
        cell_top, cell_right, cell_bottom, cell_left = self.get_coord_borders(row, col)
        tile_top, tile_right, tile_bottom, tile_left = tile.get_borders(permutation)

        if cell_top and not cell_top == tile_top:
            return False
        if cell_right and not cell_right == tile_right:
            return False
        if cell_bottom and not cell_bottom == tile_bottom:
            return False
        if cell_left and not cell_left == tile_left:
            return False

        return True

    # Returns a complete board state if solvable, None if not
    def solve(self):
        next_coord = None
        for row in range(self.board_size):
            for col in range(self.board_size):
                if (row, col) in self.placed_tiles:
                    continue
                next_coord = (row, col)
                break

        if not next_coord:
            return self

        tile_ids_to_check = []
        if self.coord_is_corner(*next_coord):
            tile_ids_to_check += corners
        if self.coord_is_border(*next_coord):
            tile_ids_to_check += borders
        tile_ids_to_check += inners

        for tile_id_to_check in tile_ids_to_check:
            if tile_id_to_check not in self.unused_tile_ids:
                continue
            for permutation in range(8):
                if self.can_place_tile(*next_coord, tile_id_to_check, permutation):
                    sub_board = self.place_tile(*next_coord, tile_id_to_check, permutation)
                    solved = sub_board.solve()
                    if solved:
                        return solved
        return None

    def corner_ids(self):
        corners = []
        for coord in ((0, 0),
                      (0, self.board_size - 1),
                      (self.board_size - 1, 0),
                      (self.board_size - 1, self.board_size - 1)):
            corners.append(self.placed_tiles[coord][0])
        return corners





all_tiles = build_tiles_from_file("input.txt")
size = determine_board_size(all_tiles)
neighbors_dict = build_neighbor_count_dict(all_tiles)
corners, borders, inners = sort_tiles(neighbors_dict)

start_board = Board(size)
start_board.update_unused_tile_ids()
solved = start_board.solve()

if solved:
    corners = solved.corner_ids()
    print(corners)
    total = 1
    for x in corners:
        total *= x
    print(total)


print("")



