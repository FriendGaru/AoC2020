class Waiting_Area:
    def __init__(self):
        self.rows = []

    def build_from_file(self, filename):
        with open(filename) as file:
            self.rows = []
            for line in file:
                line = line.strip()
                self.rows.append([char for char in line])

    def display(self):
        for row in self.rows:
            print("".join(row))
        print()

    def get_cell(self, row, col):
        if 0 <= row < len(self.rows) and 0 <= col < len(self.rows[row]):
            return self.rows[row][col]
        else:
            return None

    def update_cell(self, row, col):
        initial_state = self.get_cell(row, col)
        adj_occ = 0
        for _row in (row -1, row, row+1):
            for _col in (col -1, col, col+1):
                if row == _row and _col == col:
                    continue
                if self.get_cell(_row, _col) == "#":
                    adj_occ += 1
        if initial_state == 'L' and adj_occ == 0:
            return "#", True
        elif initial_state == "#" and adj_occ >= 4:
            return "L", True
        else:
            return initial_state, False

    def next_state(self):
        change_found = False
        new_rows = []
        for row in range(len(self.rows)):
            new_row = []
            for col in range(len(self.rows[row])):
                new_cell, change = self.update_cell(row, col)
                if change:
                    change_found = True
                new_row.append(new_cell)
            new_rows.append(new_row)
        return new_rows, change_found

    def count_char(self, char):
        count = 0
        for row in range(len(self.rows)):
            for col in range(len(self.rows[row])):
                if self.rows[row][col] == char:
                    count += 1
        return count

    def find_stable(self):
        iters = 0
        while True:
            iters += 1
            next_state, change_found = self.next_state()
            if not change_found:
                self.display()
                print("Iterations: " + str(iters))
                print("Occupied: " + str(self.count_char("#")))
                break
            else:
                self.rows = next_state








wait = Waiting_Area()
wait.build_from_file("input.txt")
wait.display()

wait.find_stable()

