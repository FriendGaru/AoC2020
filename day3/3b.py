class Terrain:
    def __init__(self, input_file):
        self.rows = []
        with open(input_file) as file:
            for line in file:
                self.rows.append(line.strip())
        self.width = len(self.rows[0])
        self.height = len(self.rows)
        for row in self.rows:
            assert len(row) == self.width

    def check_tile(self, row, col):
        assert 0 <= row < self.height
        col = col % self.width
        if self.rows[row][col] == "#":
            return True
        else:
            return False


slopes_to_check = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
tree_counts = []



terrain = Terrain("input.txt")
for slope in slopes_to_check:
    current_pos = (0, 0)
    tree_count = 0
    while current_pos[0] < terrain.height:
        if terrain.check_tile(*current_pos):
            tree_count += 1
        current_pos = (current_pos[0] + slope[0], current_pos[1] + slope[1])
    tree_counts.append(tree_count)

print(tree_counts)
total = 1
for tree_count in tree_counts:
    total *= tree_count

print(total)
