import os.path

from common.common import download_input_if_not_exists, post_answer, capture, capture_all, read_input_lines

download_input_if_not_exists(2025)

def part1(lines):
    start = str.index(lines[0], 'S')
    beams = [(start, 0)]  # (x, y)
    splits = set()
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
            beams.append((new_b_pos[0] - 1, new_b_pos[1]))
            beams.append((new_b_pos[0] + 1, new_b_pos[1]))
            splits.add(f"{new_b_pos[0]},{new_b_pos[1]}")
    return len(splits)

def part2(lines):
    start = str.index(lines[0], 'S')
    beams = [(start, 0, f"({start},0)")]  # (x, y)
    already_dones = set()
    paths = set()
    while len(beams) > 0:
        b = beams.pop(0)
        if b in already_dones:
            continue
        already_dones.add(b)
        new_b_pos = (b[0], b[1] + 1)
        if new_b_pos[1] >= len(lines):
            paths.add(b[2])
            continue
        if lines[new_b_pos[1]][new_b_pos[0]] == '.':
            next_beam = (new_b_pos[0], new_b_pos[1], f"{b[2]}->{new_b_pos}")
            beams.append(next_beam)
        elif lines[new_b_pos[1]][new_b_pos[0]] == '^':

            if new_b_pos[0]-1  >= 0:
                next_beam_left = (new_b_pos[0] - 1, new_b_pos[1], f"{b[2]}->{(new_b_pos[0]-1, new_b_pos[1])}")
                beams.append(next_beam_left)

            if new_b_pos[0]+1 < len(lines[0]):
                next_beam_right = (new_b_pos[0] + 1, new_b_pos[1], f"{b[2]}->{(new_b_pos[0]+1, new_b_pos[1])}")
                beams.append(next_beam_right)

    return len(paths)


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
