import os.path
from collections import defaultdict

from common.common import download_input_if_not_exists, post_answer, capture, capture_all, read_input_lines

download_input_if_not_exists(2025)

def part1(lines):
    final_result = 0
    operands = defaultdict(list)
    for i in range(len(lines)-1):
        values = capture_all(r"(\d+)", lines[i])
        for j in range(len(values)):
            operands[j].append(int(values[j]))
    operators = capture_all(r"([+\-*\/])", lines[-1])

    for i in range(len(operators)):
        op = operators[i]
        vals = operands[i]

        to_compute = ""
        for v in vals:
            to_compute += str(v)
            if op == '+':
                to_compute += '+'
            elif op == '-':
                to_compute += '-'
            elif op == '*':
                to_compute += '*'
            elif op == '/':
                to_compute += '/'

        result = eval(to_compute[:-1])  # Remove the last operator
        print(result)
        final_result += result

    return final_result


def part2(lines):
    operators = capture_all(r"([+\-*\/])", lines[-1])

    # rotate lines counter-clockwise
    rotated_lines = defaultdict(list)
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            rotated_lines[x] = rotated_lines.get(x, "") + lines[y][x]

    operands = defaultdict(list)
    i = 0
    cur_op = ""
    final_result = 0
    for _,v in rotated_lines.items():
        v = v.replace(" ", "")
        try:
            operand = capture(r"(\d+)", v)
            cur_op += operand[0] + operators[i]
        except ValueError:
            sub_result = eval(cur_op[:-1])  # Remove last operator
            final_result += sub_result
            print(sub_result)
            i += 1
            cur_op = ""

    # dont forget last one
    sub_result = eval(cur_op[:-1])  # Remove last operator
    final_result += sub_result


    #print(rotated_lines)

    return final_result


if __name__ == '__main__':

    part = 2
    expectedSampleResult = 4277556
    expectedSampleResult2 = 3263827

    part_func = part1 if part == 1 else part2
    expectedSampleResult = expectedSampleResult if part == 1 else expectedSampleResult2
    if part_func(read_input_lines("sample.txt")) == expectedSampleResult:
        print(f"Sample for part {part} OK")

        result = part_func(read_input_lines("input.txt"))
        print(f"Input result for part {part} is {result}")

        post_answer(2025, part, result)
        print(f"Part {part} result posted !")
    else:
        print(f"Sample for part {part} FAILED")
