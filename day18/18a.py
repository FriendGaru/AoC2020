import re

def tokenize_math_line(math_line):
    # math_line = math_line.strip()
    # math_line = math_line.replace("(", " ( ")
    # math_line = math_line.replace(")", " ) ")
    # math_line = math_line.strip()
    # while "  " in math_line:
    #     math_line = math_line.replace("  ", " ")
    # math_line_parts = math_line.split(" ")
    # return math_line_parts
    math_line = math_line.replace(" ", "")
    math_line = math_line.replace("−","-")
    return list(filter(None, re.split(r"([\(\)\+\-\/\*])", math_line)))


OPERATORS = ("+", "-", "*", "/")

PRECEDENCE = {
    "+": 1,
    "-": 1,
    "*": 1,
    "/": 1,
}

def numerize(input_string):
    try:
        return float(input_string)
    except ValueError:
        return None

def solve(math_line):
    tokens = tokenize_math_line(math_line)
    output_queue = []
    operator_stack = []
    # Shunting Yard Algorithm
    while tokens:
        next_token = tokens.pop(0)
        numerized_token = numerize(next_token)
        if numerized_token:
            output_queue.append(numerized_token)
        elif next_token in OPERATORS:
            while operator_stack and operator_stack[-1] in OPERATORS and\
                    PRECEDENCE[operator_stack[-1]] >= PRECEDENCE[next_token]:
                output_queue.append(operator_stack.pop())
            operator_stack.append(next_token)
        elif next_token == "(":
            operator_stack.append("(")
        elif next_token == ")":
            while not operator_stack[-1] == "(":
                output_queue.append(operator_stack.pop())
            operator_stack.pop()
        else:
            raise ValueError("Token problem!")
    while operator_stack:
        output_queue.append(operator_stack.pop())

    # Output queue is reverse Polish notation
    rpn_stack = []
    while output_queue:
        next_token = output_queue.pop(0)
        numerized_token = numerize(next_token)
        if numerized_token:
            rpn_stack.append(numerized_token)
        elif next_token == "+":
            val = rpn_stack.pop() + rpn_stack.pop()
            rpn_stack.append(val)
        elif next_token == "-":
            val = -rpn_stack.pop() + rpn_stack.pop()
            rpn_stack.append(val)
        elif next_token == "*":
            val = rpn_stack.pop() * rpn_stack.pop()
            rpn_stack.append(val)
        elif next_token == "/":
            denomenator, numerator = rpn_stack.pop(), rpn_stack.pop()
            rpn_stack.append(numerator / denomenator)

    return rpn_stack[0]

total = 0
with open("input.txt") as file:
    for line in file:
        line = line.strip()
        total += solve(line)
print(total)