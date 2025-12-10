import os.path

from common.common import download_input_if_not_exists, post_answer, capture, capture_all, read_input_lines
from day10.Graph import Graph

download_input_if_not_exists(2025)

def read_patterns_and_buttons(lines):
    patterns_by_id = []
    buttons_by_id = []
    joltages_by_id = []
    for l in lines:
        target_pattern = capture_all(r"[#.]+", l)
        patterns_by_id.append(target_pattern[0])

        available_buttons = capture_all(r"([0-9,]+)", l)
        buttons = []
        for b in available_buttons:
            buttons.append([int(bb) for bb in b.split(',')])
        buttons_by_id.append(buttons[:-1])
        joltages_by_id.append(buttons[-1])

    return patterns_by_id, buttons_by_id, joltages_by_id


def get_all_possible_combinations(length):
    if length == 0:
        return [""]

    smaller_combinations = get_all_possible_combinations(length - 1)
    combinations = []
    for sc in smaller_combinations:
        combinations.append(sc + ".")
        combinations.append(sc + "#")
    return combinations

def part1(lines):
    patterns_by_id, buttons_by_id, _ = read_patterns_and_buttons(lines)

    # for i in range(len(patterns_by_id)):
    #     pattern = patterns_by_id[i]
    #     buttons = buttons_by_id[i]
    #
    #     print(pattern)
    #     print(buttons)
    #     print("---")
    res = 0
    for i in range(len(patterns_by_id)):
        p = patterns_by_id[i]
        b = buttons_by_id[i]
        g = Graph()
        start = "." * len(p)
        combinations = get_all_possible_combinations(len(p))
        for c in combinations:
            for button in b:
                target = list(c)
                for pos in button:
                    target[pos] = '#' if target[pos] == '.' else '.'
                output_pattern = "".join(target)
                g.add_edge(c, output_pattern, 1)

        distance, path = g.shortest_path(start, p)
        res += distance
    #print(distance, path)

    return res




def part2(lines):
    return 4


if __name__ == '__main__':

    part = 1
    expectedSampleResult = 7
    expectedSampleResult2 = -1

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
