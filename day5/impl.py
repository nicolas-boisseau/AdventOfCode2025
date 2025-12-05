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

            # cas 1 : nr englobe r
            if nr[0] < r[0] and nr[1] > r[1]:
                has_overlap = True
                print("case 1")
                #print(f"nr: {nr}, r: {r}")
                # nr should be split into 2 new ranges
                if r[0]-1 >= nr[0]:
                    nr1 = [nr[0], r[0]-1]
                    fixed_nr.append(nr1)

                if r[1] + 1 <= nr[1]:
                    nr2 = [r[1]+1, nr[1]]
                    fixed_nr.append(nr2)
                break
            # elif nr[0] <= r[0] and nr[1] > r[1]: # cas 1 bis
            #     has_overlap = True
            #     print("case 1 bis")
            #     # nr should be split into 2 new ranges
            #     nr1 = [nr[0], r[0] - 1]
            #     nr2 = [r[1] + 1, nr[1]]
            #     fixed_nr.append(nr1)
            #     fixed_nr.append(nr2)
            #     break

            # cas 2 : r englobe nr : rien à faire
            #
            elif nr[0] <= r[0] and nr[1] >= r[1]:
                has_overlap = True
                print("case 2")
                # rien à faire
            #     has_overlap = True
            #     # nr is removed
            #     nr = None

            # cas 3 : overlap à gauche
            elif nr[0] <= r[1] and r[1] <= nr[1]:
                print("case 3")
                has_overlap = True
                if r[1]+1 <= nr[1]:
                    fixed_nr.append([r[1]+1, nr[1]])
                break

            # cas 4 : overlap à droite
            elif nr[0] <= r[0] and r[0] <= nr[1]:
                print("case 4")
                has_overlap = True
                if nr[0] <= r[0]-1:
                    fixed_nr.append([nr[0], r[0]-1])
                break

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
