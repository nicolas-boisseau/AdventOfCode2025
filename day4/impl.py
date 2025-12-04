import os.path

from common.common import download_input_if_not_exists, post_answer, capture, capture_all, read_input_lines

download_input_if_not_exists(2025)

def part1(lines):
    res = 0
    newlines = []
    for y in range(len(lines)):
        curr_line = ""
        for x in range(len(lines[y])):
            if lines[y][x] == '.':
                #print(lines[y][x], end='')
                curr_line+="."
                pass
            else:
                count = 0
                for yy in range(y-1, y+2):
                    for xx in range(x-1, x+2):
                        if yy >= 0 and yy < len(lines) and xx >= 0 and xx < len(lines[yy]):
                            if (yy != y or xx != x) and lines[yy][xx] == "@":
                                count += 1
                if count < 4:
                    res+=1
                    #print("x", end='')
                    curr_line+="."
                else:
                    #print("@", end='')
                    curr_line+="@"
        #print()
        newlines.append(curr_line)
    #print(res)
    #print(newlines)
    return res, newlines


def part2(lines):
    res = 0
    curr_res, lines = part1(lines)
    res += curr_res
    while curr_res > 0:
        curr_res, lines = part1(lines)
        res+=curr_res
    return res

if __name__ == '__main__':

    part = 2
    expectedSampleResult = 13
    expectedSampleResult2 = 43

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
