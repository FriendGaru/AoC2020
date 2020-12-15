def build_program(filename):
    with open(filename) as file:
        program = []
        for line in file:
            line = line.strip()
            line_parts = line.split("=")
            if line_parts[0] == "mask ":
                program.append(("mask", line_parts[1]))
            elif line_parts[0].startswith("mem"):
                address = int(line_parts[0].split("[")[1].replace("]", ""))
                val = int(line_parts[1])
                program.append(("mem", address, val))
    return program

class VM:
    def __init__(self):
        self.and_mask = None
        self.or_mask = None
        self.memory = {}

    def set_mask(self, mask):
        self.zero_mask = 0
        self.one_mask = 0

        current_digit = 1
        for char in reversed(mask):
            if char == "1":
                self.one_mask += current_digit
            elif char == "0":
                self.zero_mask += current_digit
            current_digit *= 2

    def write_mem(self, address, val):
        val = val | self.one_mask
        val = val & ~self.zero_mask
        self.memory[address] = val

    def run_program(self, program):
        for command in program:
            if command[0] == "mask":
                self.set_mask(command[1])
            elif command[0] == "mem":
                self.write_mem(command[1], command[2])

    def mem_sum(self):
        return sum(self.memory.values())


vm = VM()
program = build_program("input.txt")
vm.run_program(program)

print(vm.memory)
print(vm.mem_sum())
