import math
import os.path
from collections import defaultdict

from common.common import download_input_if_not_exists, post_answer, capture, capture_all, read_input_lines

download_input_if_not_exists(2025)

def is_in_any_circuit(circuits, n1, n2):
    for k,v in circuits.items():
        if n1 in v and n2 in v:
            return k, None
        elif n1 in v or n2 in v:
            return k, n1 if n1 in v else n2
    return None, None

def part1(lines, max_connections=10):
    positions = []
    for l in lines:
        x,y,z = [int(c) for c in l.split(",")]
        positions.append( (x,y,z) )

    circuits = defaultdict(list)
    already_connected = set()
    for i in range(max_connections):
        min_dist = 99999999999999
        min_couple = (None,None)
        for x,y,z in positions:
            for x2,y2,z2 in positions:
                if (x,y,z) != (x2,y2,z2) and ((x,y,z),(x2,y2,z2)) not in already_connected and ((x2,y2,z2),(x,y,z)) not in already_connected:
                    dist = math.sqrt( (x2-x)**2 + (y2-y)**2 + (z2-z)**2 )
                    if dist < min_dist:
                        min_dist = dist
                        min_couple = ( (x,y,z), (x2,y2,z2) )

        circuit_id, node_already_in = is_in_any_circuit(circuits, min_couple[0], min_couple[1])
        if circuit_id is None:
            k = min_couple[0]
            circuits[k].append(min_couple[0])
            circuits[k].append(min_couple[1])
        else:
            if node_already_in == min_couple[0]:
                circuits[circuit_id].append(min_couple[1])
            else:
                circuits[circuit_id].append(min_couple[0])

        already_connected.add(min_couple)
        already_connected.add((min_couple[1], min_couple[0]))

    for c in circuits:
        print(len(c))
    print(positions)
    return 0


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
