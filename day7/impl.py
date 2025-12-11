import os.path
from collections import defaultdict

from common.common import download_input_if_not_exists, post_answer, capture, capture_all, read_input_lines

download_input_if_not_exists(2025)

def part1_ext(lines):
    start = str.index(lines[0], 'S')
    beams = [(start, 0)]  # (x, y)
    splits = defaultdict(int)
    already_dones = set()
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
            if not (new_b_pos[0] - 1, new_b_pos[1]) in beams:
                beams.append((new_b_pos[0] - 1, new_b_pos[1]))
            if not (new_b_pos[0] + 1, new_b_pos[1]) in beams:
                beams.append((new_b_pos[0] + 1, new_b_pos[1]))
            splits[new_b_pos[1]] += 1
    return sum([splits[k] for k in splits]), splits

def part1(lines):
    return part1_ext(lines)[0]

def part2(lines):
    start = str.index(lines[0], 'S')
    timelines = defaultdict(int)
    timelines[start] = 1

    def print_timelines(timelines, y):
        for x in range(0, len(lines[y])):
            if x in timelines:
                print(timelines[x], end="")
            else:
                print(".", end="")
        print()

    for y in range(len(lines)-1):
        print_timelines(timelines, y)
        x_positions = timelines.keys()
        new_timelines = defaultdict(int)
        for x in x_positions:
            count = timelines[x]
            if lines[y+1][x] == '.':
                new_timelines[x] += count
            elif lines[y+1][x] == '^':
                new_timelines[x - 1] += count
                new_timelines[x + 1] += count
        timelines = new_timelines

    return sum([timelines[k] for k in timelines])




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
