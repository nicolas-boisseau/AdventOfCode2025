import os.path

from common.common import download_input_if_not_exists, post_answer, capture, capture_all, read_input_lines

download_input_if_not_exists(2025)

def extract_presents_and_trees(lines):
    presents = {}
    trees = {}
    cur_id = -1
    cur_pattern = []
    for l in lines:
        if "x" in l:
            splitted = l.split(": ")
            splitted2 = splitted[0].split("x")
            tree_size = (int(splitted2[0]), int(splitted2[1]))
            tree_requirements = [int(c) for c in splitted[1].split(" ")]
            trees[tree_size] = tree_requirements
        elif ':' in l:
            cur_id = int(l.split(":")[0])
        elif l != "":
            cur_pattern.append(l)
        else:
            presents[cur_id] = cur_pattern
            cur_pattern = []
            cur_id = -1

    # for p in presents:
    #     pattern = presents[p]
    #     print(f"Present {p}:")
    #     for line in pattern:
    #         print(line)
    #     print("")
    #
    # for t in trees:
    #     print(f"Tree size {t}: requirements {trees[t]}")

    return presents, trees

def print_tree_grid(grid):
    for row in grid:
        print("".join(row))
    print()

def part1(lines):
    presents, trees = extract_presents_and_trees(lines)

    for t in trees:
        grid = [["." for _ in range(t[0])] for _ in range(t[1])]
        print_tree_grid(grid)

        requirements = trees[t]
        print(f"Tree size {t} requires {requirements} presents")
        for i in range(len(requirements)):
            number_of_occurrences = requirements[i]
            pattern = presents[i]

            for j in range(number_of_occurrences):

                print(f"Placing {number_of_occurrences} present {i} with pattern:")
                for line in pattern:
                    print(line)
                print()

                # check if pattern can fit in the grid
                pattern_height = len(pattern)
                pattern_width = len(pattern[0])
                placed = False
                for y in range(t[1] - pattern_height + 1):
                    for x in range(t[0] - pattern_width + 1):
                        can_place = True
                        for py in range(pattern_height):
                            for px in range(pattern_width):
                                if pattern[py][px] == "#" and grid[y + py][x + px] == "#":
                                    can_place = False
                                    break
                            if not can_place:
                                break
                        if can_place:
                            # place the pattern
                            for py in range(pattern_height):
                                for px in range(pattern_width):
                                    if pattern[py][px] == "#":
                                        grid[y + py][x + px] = "#"
                            placed = True
                            print(f"Placed present {i} at position ({x}, {y})")
                            print_tree_grid(grid)
                            break
                    if placed:
                        break
                if not placed:
                    print(f"Could not place present {i} on the tree of size {t}")






    return 3


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
