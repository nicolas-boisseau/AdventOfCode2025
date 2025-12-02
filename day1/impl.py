import os.path

from common.common import download_input_if_not_exists, post_answer, capture, capture_all, read_input_lines

download_input_if_not_exists(2025)

def part1(lines):
    pos=50
    res=0
    print("OK")
    for l in lines:
        d=l[0]
        n=int(l[1:])
        if d == "R":
            pos+=n
        else:
            pos-=n
        pos=pos%100
        res+=(1 if pos == 0 else 0)
        print(pos)

    print(f"Result: {res}")
    return res
    


def part2(lines):
    pos = 50
    res = 0
    print("OK")
    for l in lines:
        d = l[0]
        n = int(l[1:])
        if d == "R":
            while n > 0:
                pos+=1
                n-=1
                if pos == 100:
                    pos = 0
                if pos == 0:
                    res+=1

        else:
            while n > 0:
                pos -= 1
                n -= 1
                if pos == -1:
                    pos = 99
                if pos == 0:
                    res += 1

        # pass_zero = abs(pos // 100)
        # pos = pos % 100
        # res += pass_zero
        # print(pos)

    print(f"Result 2: {res}")
    return res


if __name__ == '__main__':

    part = 2
    expectedSampleResult = 6

    part_func = part1 if part == 1 else part2
    if part_func(read_input_lines("sample.txt")) == expectedSampleResult:
        print(f"Sample for part {part} OK")

        result = part_func(read_input_lines("input.txt"))
        print(f"Input result for part {part} is {result}")

        #post_answer(2025, part, result)
        print(f"Part {part} result posted !")
    else:
        print(f"Sample for part {part} FAILED")
