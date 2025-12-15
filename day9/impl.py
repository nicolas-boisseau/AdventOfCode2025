import os.path
from collections import defaultdict
import numpy as np
from shapely.geometry import Point, Polygon

from common.common import download_input_if_not_exists, post_answer, capture, capture_all, read_input_lines

download_input_if_not_exists(2025)

def part1(lines):
    positions = []
    for l in lines:
        x, y = [int(c) for c in l.split(",")]
        positions.append((x, y))

    d = defaultdict(int)
    for x, y in positions:
        for x2, y2 in positions:
            if (x, y) != (x2, y2):
                if ((x, y), (x2, y2)) not in d and ((x2, y2), (x, y)) not in d:
                    d[((x, y), (x2, y2))] = abs(x - x2) + abs(y - y2)

    # sort d using its values
    sorted_d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))

    print(sorted_d)

    best = list(sorted_d.keys())[0]
    a = best[0]
    b = best[1]
    # compute the area
    area = (abs(a[0] - b[0])+1) * (abs(a[1] - b[1])+1)
    print(area)


    return area

def get_corners_points(lines) -> list[tuple[int, int]]:
    allpoints = []
    for l in lines:
        x, y = [int(c) for c in l.split(",")]
        allpoints.append((x, y))
    return allpoints


def trace_all_points(lines) -> list[tuple[int, int]]:
    allpoints = []
    max_x = 0
    max_y = 0
    lines.append(lines[0])  # close the shapes
    for l in lines:
        x, y = [int(c) for c in l.split(",")]
        max_x = max(max_x, x)
        max_y = max(max_y, y)
        if len(allpoints) > 0:
            lastx, lasty = allpoints[-1]
            if x != lastx:
                step = 1 if x > lastx else -1
                for nx in range(lastx, x, step):
                    allpoints.append((nx, lasty))
            if y != lasty:
                step = 1 if y > lasty else -1
                for ny in range(lasty, y, step):
                    allpoints.append((x, ny))
        if (x, y) not in allpoints:
            allpoints.append((x, y))
    return allpoints

def print_points(allpoints_set=None, inside_set=None):
    max_y = max([y for (x, y) in allpoints_set])
    max_x = max([x for (x, y) in allpoints_set])
    for y in range(max_y + 2):
        for x in range(max_x + 2):
            if (x, y) in allpoints_set:
                print("#", end="")
            elif (x, y) in inside_set:
                print("o", end="")
            else:
                print(".", end="")
        print("")

def compute_best_area(lines: str, corner_points: list[tuple[int,int]], polygon: Polygon) -> int:
    positions = []
    for l in lines:
        x, y = [int(c) for c in l.split(",")]
        positions.append((x, y))

    d = defaultdict(int)
    for x, y in positions:
        for x2, y2 in positions:
            if (x, y) != (x2, y2):
                if ((x, y), (x2, y2)) not in d and ((x2, y2), (x, y)) not in d:
                    d[((x, y), (x2, y2))] = abs(x - x2) + abs(y - y2)

    # sort d using its values
    sorted_d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))

    # print(sorted_d)

    all_bests = list(sorted_d.keys())
    while len(all_bests) > 0:
        next_best = all_bests.pop(0)
        a = next_best[0]
        b = next_best[1]

        rectangle = Polygon([(a[0], a[1]), (b[0], a[1]), (b[0], b[1]), (a[0], b[1])])

        # check if rectangle is fully inside polygon
        if polygon.contains(rectangle):
            # compute the area
            area = (abs(a[0] - b[0])+1) * (abs(a[1] - b[1])+1)
            print(area)
            return area
    return 0

def part2(lines):

    print("1. get all corners")
    corners_points = get_corners_points(lines)
    #allpoints = trace_all_points(lines)

    #print_points(allpoints_set, set())

    print("2. Create polygon")
    # Define the polygon
    polygon = Polygon(corners_points)

    print("3. compute best area")
    best_area = compute_best_area(lines, corners_points, polygon)
    print("Best area is ", best_area)

    return best_area





if __name__ == '__main__':

    part = 1
    expectedSampleResult = 50
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
