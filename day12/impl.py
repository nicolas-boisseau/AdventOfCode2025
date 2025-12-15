import os.path

from common.common import download_input_if_not_exists, post_answer, capture, capture_all, read_input_lines

download_input_if_not_exists(2025)

def extract_presents_and_trees(lines):
    presents = {}
    presents_sizes = {}
    trees = {}
    t_id = 0
    cur_id = -1
    cur_pattern = []
    for l in lines:
        if "x" in l:
            splitted = l.split(": ")
            splitted2 = splitted[0].split("x")
            tree_size = (int(splitted2[0]), int(splitted2[1]))
            tree_requirements = [int(c) for c in splitted[1].split(" ")]
            trees[t_id] = (tree_size, tree_requirements)
            t_id += 1
        elif ':' in l:
            cur_id = int(l.split(":")[0])
        elif l != "":
            cur_pattern.append(l)
        else:
            presents[cur_id] = cur_pattern
            presents_sizes[cur_id] = sum([1 if c == "#" else 0 for c in "".join(cur_pattern)])
            cur_pattern = []
            cur_id = -1

    # for p in presents:
    #     pattern = presents[p]
    #     size = presents_sizes[p]
    #     print(f"Present {p} (size = {size}:")
    #     for line in pattern:
    #         print(line)
    #     print("")
    #
    # for t in trees:
    #     print(f"Tree size {t}: requirements {trees[t]}")

    return presents, presents_sizes, trees

def print_tree_grid(grid):
    for row in grid:
        print("".join(row))
    print()

def part1(lines):
    presents, presents_sizes, trees = extract_presents_and_trees(lines)

    res = 0
    for i in range(len(trees)):
        t = trees[i]
        tree_size = t[0][0] * t[0][1]
        requirements = t[1]
        #print(f"Tree size {t} requires {requirements} presents")
        req_size = 0
        for i in range(len(requirements)):
            req_size += requirements[i] * presents_sizes[i]

        if tree_size >= req_size:
            res += 1

    return res


def part2(lines):
    return 4


if __name__ == '__main__':

    part = 1
    expectedSampleResult = -1
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
