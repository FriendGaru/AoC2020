class Waiting_Area:
    def __init__(self):
        self.rows = []
        self.counts = []
        self.height = 0
        self.width = 0

    def build_from_file(self, filename):
        with open(filename) as file:
            self.rows = []
            for line in file:
                line = line.strip()
                self.rows.append([char for char in line])
        self.height = len(self.rows)
        self.width = len(self.rows[0])

    def blank_counts(self):
        counts = []
        for row in range(self.height):
            new_counts_row = []
            for col in range(self.width):
                new_counts_row.append(0)
            counts.append(new_counts_row)
        self.counts = counts

    def display(self):
        for row_num in range(self.height):
            print("".join(self.rows[row_num]) + " | " + "".join([str(x) for x in self.counts[row_num]]))
        print("Occupied: " + str(self.count_char("#")))

    def get_cell(self, row, col):
        if 0 <= row < len(self.rows) and 0 <= col < len(self.rows[row]):
            return self.rows[row][col]
        else:
            return None

    def get_cell_count(self, row, col):
        if 0 <= row < len(self.rows) and 0 <= col < len(self.rows[row]):
            return self.counts[row][col]
        else:
            return None

    def update_counts(self):
        for row_num in range(self.height):
            self.update_row_counts(row_num)
        for col_num in range(self.width):
            self.update_col_counts(col_num)

        # #Top-left to bottom right
        # #Starting top row
        for col_num in range(self.width):
            self.update_diag_topleft_bottomright_counts(0, col_num)
        # # # Starting left col
        for row_num in range(1, self.height):
            self.update_diag_topleft_bottomright_counts(row_num, 0)

        # Bottom left to top right
        # Starting top row
        for col_num in range(self.width):
            self.update_diag_bottomleft_topright_counts(0, col_num)
        # Starting right col
        for row_num in range(1, self.height):
            self.update_diag_bottomleft_topright_counts(row_num, self.width-1)
        pass


    def update_row_counts(self, row_num):
        # Ascending
        occupied_found = False
        for check_col in range(self.width):
            if occupied_found:
                self.counts[row_num][check_col] += 1
            if self.get_cell(row_num, check_col) == "#":
                occupied_found = True
            elif self.get_cell(row_num, check_col) == "L":
                occupied_found = False

        # Descending
        occupied_found = False
        for check_col in range(self.width-1, -1, -1):
            if occupied_found:
                self.counts[row_num][check_col] += 1
            if self.get_cell(row_num, check_col) == "#":
                occupied_found = True
            elif self.get_cell(row_num, check_col) == "L":
                occupied_found = False

    def update_col_counts(self, col_num):
        # Ascending
        occupied_found = False
        for check_row in range(self.height):
            if occupied_found:
                self.counts[check_row][col_num] += 1
            if self.get_cell(check_row, col_num) == "#":
                occupied_found = True
            elif self.get_cell(check_row, col_num) == "L":
                occupied_found = False

        # Descending
        occupied_found = False
        for check_row in range(self.height-1, -1, -1):
            if occupied_found:
                self.counts[check_row][col_num] += 1
            if self.get_cell(check_row, col_num) == "#":
                occupied_found = True
            elif self.get_cell(check_row, col_num) == "L":
                occupied_found = False

    def update_diag_topleft_bottomright_counts(self, row_num, col_num):
        # row ascending, col ascending
        occupied_found = False
        check_row = row_num
        check_col = col_num
        while check_row < self.height and check_col < self.width:
            if occupied_found:
                self.counts[check_row][check_col] += 1
            if self.get_cell(check_row, check_col) == "#":
                occupied_found = True
            elif self.get_cell(check_row, check_col) == "L":
                occupied_found = False
            check_row += 1
            check_col += 1

        # row descending, col descending
        occupied_found = False
        while check_row >= 0 and check_col >= 0:
            if occupied_found:
                self.counts[check_row][check_col] += 1
            if self.get_cell(check_row, check_col) == "#":
                occupied_found = True
            elif self.get_cell(check_row, check_col) == "L":
                occupied_found = False
            check_row -= 1
            check_col -= 1

    def update_diag_bottomleft_topright_counts(self, row_num, col_num):
        # row ascending, col descending
        occupied_found = False
        check_row = row_num
        check_col = col_num
        while check_row < self.height and check_col >= 0:
            if occupied_found:
                self.counts[check_row][check_col] += 1
            if self.get_cell(check_row, check_col) == "#":
                occupied_found = True
            elif self.get_cell(check_row, check_col) == "L":
                occupied_found = False
            check_row += 1
            check_col -= 1

        # row descending, col descending
        occupied_found = False
        while check_row >= 0 and check_col < self.width:
            if occupied_found:
                self.counts[check_row][check_col] += 1
            if self.get_cell(check_row, check_col) == "#":
                occupied_found = True
            elif self.get_cell(check_row, check_col) == "L":
                occupied_found = False
            check_row -= 1
            check_col += 1

    def update_occupancies(self):
        change_made = False
        for row_num in range(self.height):
            for col_num in range(self.width):
                current_state = self.get_cell(row_num, col_num)
                cell_count = self.counts[row_num][col_num]
                if current_state == "#" and cell_count >= 5:
                    self.rows[row_num][col_num] = "L"
                    change_made = True
                elif current_state == "L" and cell_count == 0:
                    self.rows[row_num][col_num] = "#"
                    change_made = True
                self.counts[row_num][col_num] = 0
        return change_made

    def count_char(self, char):
        count = 0
        for row in range(len(self.rows)):
            for col in range(len(self.rows[row])):
                if self.rows[row][col] == char:
                    count += 1
        return count


wait = Waiting_Area()
wait.build_from_file("input.txt")
wait.blank_counts()
# wait.display()

while True:
    wait.update_counts()
    wait.display()
    change_found = wait.update_occupancies()

    if not change_found:
        break

pass