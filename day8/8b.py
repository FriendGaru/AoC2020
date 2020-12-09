class VirtualMachine:
    def __init__(self, code_file):
        self.code = []
        with open(code_file) as file:
            for line in file:
                line = line.strip()
                if line == "":
                    continue
                instruction = line[0:3]
                val = int(line[4:])
                self.code.append((instruction, val))
        self.executed_lines = set()
        self.accumulator = 0
        self.program_counter = 0

    def acc(self, val):
        self.accumulator += val
        self.program_counter += 1

    def jmp(self, val):
        self.program_counter += val

    def nop(self, val):
        self.program_counter += 1

    def terminate(self):
        print('Program terminated')
        print("Accumulator: " + str(self.accumulator))

    def run(self):
        while True:

            # Check for termination
            if self.program_counter == len(self.code):
                self.terminate()
                return 0

            next_ins, next_val = self.code[self.program_counter]
            if self.program_counter in self.executed_lines:
                print("Endless Loop")
                print("Accumulator:" + str(self.accumulator))
                return -1
            else:
                self.executed_lines.add(self.program_counter)
            if next_ins == "acc":
                self.acc(next_val)
            elif next_ins == "jmp":
                self.jmp(next_val)
            elif next_ins == "nop":
                self.nop(next_val)
            else:
                raise ValueError("Invalid instruction: " + next_ins)

# 626 lines of code
current_line_check = 0
while current_line_check < 626:
    vm = VirtualMachine("input.txt")
    if vm.code[current_line_check][0] == "nop":
        vm.code[current_line_check] = ("jmp", vm.code[current_line_check][1])
    elif vm.code[current_line_check][0] == "jmp":
        vm.code[current_line_check] = ("nop", vm.code[current_line_check][1])
    else:
        current_line_check += 1
        continue
    output = vm.run()
    if output == 0:
        break
    else:
        current_line_check += 1
