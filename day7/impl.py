import os.path
from collections import defaultdict

from common.common import download_input_if_not_exists, post_answer, capture, capture_all, read_input_lines

download_input_if_not_exists(2025)

def part1_with_splits(lines):
    start = str.index(lines[0], 'S')
    beams = [(start, 0)]  # (x, y)
    splits = set()
    already_dones = set()
    nb_p2 = 1
    while len(beams) > 0:
        b = beams.pop(0)
        if b in already_dones:
            continue
        already_dones.add(b)
        new_b_pos = (b[0], b[1] + 1)
        if new_b_pos[1] >= len(lines):
            continue
        if lines[new_b_pos[1]][new_b_pos[0]] == '.':
            beams.append(new_b_pos)
        elif lines[new_b_pos[1]][new_b_pos[0]] == '^':
            beams.append((new_b_pos[0] - 1, new_b_pos[1]))
            beams.append((new_b_pos[0] + 1, new_b_pos[1]))
            nb_p2+=2
            splits.add(f"{new_b_pos[0]},{new_b_pos[1]}")

    print(nb_p2)
    return len(splits), splits

def part1(lines):
    res, splits = part1_with_splits(lines)
    return res

def part2(lines):
    _, splits = part1_with_splits(lines)

    cur_nb_beams = 1
    total = 1
    start = str.index(lines[0], 'S')
    beams = defaultdict(list)
    beams[0] = [start]
    for y in range(len(lines)):
        nb_splits_this_line = 0
        for x in range(len(lines[y])):
            if f"{x},{y}" in splits and x in beams[y]:
                nb_splits_this_line += 1
                beams[y+1].append(x-1)
                beams[y+1].append(x+1)

        total += len(beams[y+1])

    return total


if __name__ == '__main__':

    part = 2
    expectedSampleResult = 21
    expectedSampleResult2 = 40

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
