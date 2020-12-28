def nw(x, y, z):
    return x, y + 1, z - 1


def w(x, y, z):
    return x - 1, y + 1, z


def sw(x, y, z):
    return x - 1, y, z + 1


def ne(x, y, z):
    return x + 1, y, z - 1


def e(x, y, z):
    return x + 1, y - 1, z


def se(x, y, z):
    return x, y - 1, z + 1


def get_target_tile(instruction_list: list):
    current_x = 0
    current_y = 0
    current_z = 0
    for token in instruction_list:
        if token == "se":
            current_x, current_y, current_z = se(current_x, current_y, current_z)
        elif token == "sw":
            current_x, current_y, current_z = sw(current_x, current_y, current_z)
        elif token == "w":
            current_x, current_y, current_z = w(current_x, current_y, current_z)
        elif token == "nw":
            current_x, current_y, current_z = nw(current_x, current_y, current_z)
        elif token == "ne":
            current_x, current_y, current_z = ne(current_x, current_y, current_z)
        elif token == "e":
            current_x, current_y, current_z = e(current_x, current_y, current_z)

        # print(token, current_x, current_y, current_z)
    return current_x, current_y, current_z

class Instructions:
    def __init__(self, filename):
        self.tokenized_lines = []
        with open(filename) as file:
            for line in file:
                line = line.strip()
                if line == "":
                    continue
                line_tokens = []
                line_index = 0
                while line_index < len(line):
                    remaining_line = line[line_index:]
                    if remaining_line.startswith("e"):
                        line_tokens.append("e")
                        line_index += 1
                    elif remaining_line.startswith("se"):
                        line_tokens.append("se")
                        line_index += 2
                    elif remaining_line.startswith("sw"):
                        line_tokens.append("sw")
                        line_index += 2
                    elif remaining_line.startswith("w"):
                        line_tokens.append("w")
                        line_index += 1
                    elif remaining_line.startswith("nw"):
                        line_tokens.append("nw")
                        line_index += 2
                    elif remaining_line.startswith("ne"):
                        line_tokens.append("ne")
                        line_index += 2
                    else:
                        raise ValueError
                self.tokenized_lines.append(line_tokens)
        self.current_line = 0
        self.current_token = 0


class TileBoard:
    def __init__(self):
        self.black_tiles = set()

    def flip_tile(self, x, y, z):
        if (x, y, z) in self.black_tiles:
            self.black_tiles.remove((x, y, z))
        else:
            self.black_tiles.add((x, y, z))

    def run_many_instructions(self, many_instructions_list):
        for instructions_list in many_instructions_list:
            target_x, target_y, target_z = get_target_tile(instructions_list)
            self.flip_tile(target_x, target_y, target_z)


stream = Instructions("input.txt")
board = TileBoard()
board.run_many_instructions(stream.tokenized_lines)

print(board.black_tiles)
print(len(board.black_tiles))



