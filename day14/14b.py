def build_program(filename):
    with open(filename) as file:
        program = []
        for line in file:
            line = line.strip()
            line_parts = line.split("=")
            if line_parts[0] == "mask ":
                program.append(("mask", line_parts[1].strip()))
            elif line_parts[0].startswith("mem"):
                address = int_to_36bit_str(int(line_parts[0].split("[")[1].replace("]", "")))
                val = int_to_36bit_str(int(line_parts[1]))
                program.append(("mem", address, val))
    return program

class VM:
    def __init__(self):
        self.one_digits = []
        self.floating_digits = []
        self.memory = {}

    def set_mask(self, mask):
        self.one_digits = []
        self.floating_digits = []

        for i in range(len(mask)):
            if mask[i] == "X":
                self.floating_digits.append(i)
            elif mask[i] == "1":
                self.one_digits.append(i)

    def write_mem(self, address, val):
        self.memory[address] = val

    def write_floating_mem(self, address, val):
        assert isinstance(address, str)
        for i in self.floating_digits:
            address = address[0:i] + "X" + address[i+1:]
        for i in self.one_digits:
            address = address[0:i] + "1" + address[i+1:]
        self.write_floating_mem_sub(address, val)

    def write_floating_mem_sub(self, address, val):
        assert isinstance(address, str)
        if "X" in address:
            self.write_floating_mem_sub(address.replace("X", "0", 1), val)
            self.write_floating_mem_sub(address.replace("X", "1", 1), val)
        else:
            address = int(address)
            self.write_mem(address, val)

    def run_program(self, program):
        for command in program:
            if command[0] == "mask":
                self.set_mask(command[1])
            elif command[0] == "mem":
                self.write_floating_mem(command[1], command[2])

    def mem_sum(self):
        return sum([int(x,2) for x in self.memory.values()])

def int_to_36bit_str(val):
    out = format(val, "b").zfill(36)
    return out

vm = VM()
program = build_program("input.txt")
vm.run_program(program)

# print(vm.memory)
print(vm.mem_sum())
