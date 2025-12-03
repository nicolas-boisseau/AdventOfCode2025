import os.path

from common.common import download_input_if_not_exists, post_answer, capture, capture_all, read_input_lines

download_input_if_not_exists(2025)

def part1(lines):
    res=0
    for l in lines:
        batteries = [int(c) for c in l]

        # basic approach : it works for part 1 ;)
        # best = int(f"{batteries[0]}{batteries[1]}")
        # for a in range(len(batteries)):
        #     for b in range(a, len(batteries)):
        #         if a != b:
        #             candidate = int(f"{batteries[a]}{batteries[b]}")
        #             if candidate > best:
        #                 best = candidate
        #print(best)
        #res += best

        best_number = find_best_number(batteries, 2)
        print(best_number)
        res += int(best_number)

    print(res)
    return res

def find_next_best_but_ensure_x_digits_left(batteries, x_digits_left):
    best = -1
    best_index = -1
    for i in range(len(batteries)-x_digits_left):
        if batteries[i] > best:
            best = batteries[i]
            best_index = i
    return best, best_index

def find_best_number(batteries, digits=12):
    best_number = ""
    digits_left = digits
    while digits_left > 0:
        best, best_index = find_next_best_but_ensure_x_digits_left(batteries, digits_left - 1)
        best_number += str(best)
        batteries = batteries[best_index + 1:]
        digits_left -= 1
    return best_number

def part2(lines):
    res = 0
    for l in lines:
        batteries = [int(c) for c in l]

        best_number = find_best_number(batteries, 12)
        print(best_number)
        res += int(best_number)
    print(res)
    return res



if __name__ == '__main__':

    part = 2
    expectedSampleResult = 357
    expectedSampleResult2 = 3121910778619

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
