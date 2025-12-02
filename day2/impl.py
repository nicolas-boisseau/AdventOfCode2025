import os.path

from common.common import download_input_if_not_exists, post_answer, capture, capture_all, read_input_lines

download_input_if_not_exists(2025)

def part1(lines):
    ranges=[(int(str.split(rr,'-')[0]),int(str.split(rr,'-')[1])) for rr in str.split(lines[0], ',')]
    res=0
    for r in ranges:
        for i in range(r[0],r[1]+1):
            s = str(i)
            if s[0:len(s)//2] == s[len(s)//2:]:
                res+=int(s)
    return res

def part2(lines):
    ranges = [(int(str.split(rr, '-')[0]), int(str.split(rr, '-')[1])) for rr in str.split(lines[0], ',')]
    res = 0
    for r in ranges:
        for i in range(r[0], r[1] + 1):
            s = str(i)
            for j in range(1, len(s)//2+1):
                cur=s[0:j]
                k = j
                found = True
                while k < len(s):
                    if cur != s[k:k+j]:
                        found = False
                        break
                    k = k+j
                if found:
                    res+=int(s)
                    break
    return res


    return res


if __name__ == '__main__':

    part = 2
    expectedSampleResult = 4174379265

    part_func = part1 if part == 1 else part2
    if part_func(read_input_lines("sample.txt")) == expectedSampleResult:
        print(f"Sample for part {part} OK")

        result = part_func(read_input_lines("input.txt"))
        print(f"Input result for part {part} is {result}")

        post_answer(2025, part, result)
        print(f"Part {part} result posted !")
    else:
        print(f"Sample for part {part} FAILED")
