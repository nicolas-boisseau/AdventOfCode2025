import os.path

from common.common import download_input_if_not_exists, post_answer, capture, capture_all, read_input_lines

download_input_if_not_exists(2025)

def extract_rangs_and_ingredients(lines):
    ranges = []
    i = 0
    while lines[i] != "":
        l = lines[i]
        ranges.append([int(c) for c in l.split("-")])
        i += 1
    i+=1 # skip empty line
    ingredients = []
    while i < len(lines):
        ingredients.append(int(lines[i]))
        i += 1
    return ranges, ingredients

def part1(lines):
    ranges, ingredients = extract_rangs_and_ingredients(lines)
    res = 0
    for ingredient in ingredients:
        for r in ranges:
            if ingredient >= r[0] and ingredient <= r[1]:
                res+=1
                break
    return res

def part2(lines):
    ranges, _ = extract_rangs_and_ingredients(lines)
    res = 0

    final_ranges = [ranges.pop(0)]
    while len(ranges) > 0:
        nr = ranges.pop(0)
        fixed_nr = []

        has_overlap = False
        for r in final_ranges:

            # cas 1 : overlap seulement à gauche
            if nr[0] < r[0] and (nr[1] >= r[0] and nr[1] <= r[1]):
                nr[1] = r[0]-1
                has_overlap = True
                fixed_nr.append(nr)
                break

            # cas 2 : overlap seulement à droite
            elif nr[1] > r[1] and (nr[0] >= r[0] and nr[0] <= r[1]):
                nr[0] = r[1]+1
                has_overlap = True
                fixed_nr.append(nr)
                break

            # cas 3 : le new range est inclus dans un existant
            elif nr[0] >= r[0] and nr[1] <= r[1]:
                has_overlap = True
                # nothing to do
                break

            # cas 4 : overlap total : il faut prendre les morceaux à droite et à gauche
            elif nr[0] < r[0] and nr[1] > r[1]:
                has_overlap = True
                # split in two ranges
                fixed_nr.append([nr[0], r[0]-1])
                fixed_nr.append([r[1]-1, nr[1]])

        if not has_overlap:
            final_ranges.append(nr)
        else:
            for n in fixed_nr:
                ranges.append(n)


    for r in final_ranges:
        print(f"{r[0]} - {r[1]}")
        res += (r[1] - r[0] + 1)

    return res



if __name__ == '__main__':

    part = 2
    expectedSampleResult = 3
    expectedSampleResult2 = 14

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
