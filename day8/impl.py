import math
import os.path
from collections import defaultdict

from common.common import download_input_if_not_exists, post_answer, capture, capture_all, read_input_lines

download_input_if_not_exists(2025)


def circuit_id_if_node_in(circuits, n):
    for c_id, v in circuits.items():
        if n in v:
            return c_id
    return None

def part1(lines, max_connections=10, p2=False):
    positions = []
    for l in lines:
        x,y,z = [int(c) for c in l.split(",")]
        positions.append( (x,y,z) )

    d = defaultdict(float)
    for x, y, z in positions:
        for x2, y2, z2 in positions:
            if (x,y,z) != (x2,y2,z2):
                if ((x,y,z), (x2,y2,z2)) not in d and ((x2,y2,z2),(x,y,z)) not in d:
                    d[((x,y,z), (x2,y2,z2))] = math.sqrt( (x2-x)**2 + (y2-y)**2 + (z2-z)**2 )

    # sort d using its values
    sorted_d = dict(sorted(d.items(), key=lambda item: item[1], reverse=False))

    # for k,v in sorted_d.items():
    #     if v == 0:
    #         continue
    #     print(f"{k[0]} => {k[1]} : {v}")

    i = 0
    connected = 0
    circuits = defaultdict(list)
    for couple,d in sorted_d.items():
        if not p2:
            if i >= max_connections:
                break

        n1, n2 = couple

        #print(f"Processing connection {i} : {n1} => {n2} (distance {d})")

        n1_circuit_id = circuit_id_if_node_in(circuits, n1)
        n2_circuit_id = circuit_id_if_node_in(circuits, n2)
        if n1_circuit_id is not None and n2_circuit_id is not None:
            if n1_circuit_id != n2_circuit_id:
                #print(f"Merging circuits {n1_circuit_id} and {n2_circuit_id}")
                for other_n in circuits[n2_circuit_id]:
                    if other_n not in circuits[n1_circuit_id]:
                        circuits[n1_circuit_id].append(other_n)
                del circuits[n2_circuit_id]
            # else:
            #     print("Both nodes already in same circuit, nothing to do")

        elif n1_circuit_id is not None:
            circuits[n1_circuit_id].append(n2)
        elif n2_circuit_id is not None:
            circuits[n2_circuit_id].append(n1)
        else:
            # new circuit
            circuits[i].append(n1)
            circuits[i].append(n2)

        if p2 and any([len(v) == len(positions) for k,v in circuits.items()]):
            print("All nodes connected !")
            return n1[0] * n2[0]

        i+=1

    print("Final circuits:")
    for k,v in circuits.items():
        print(f"Circuit {k} : {v}")

    lengths = [len(v) for k,v in circuits.items()]
    lengths.sort()

    print(f"Number of circuits: {len(circuits)}")
    print(f"Circuit lengths: {lengths}")

    return lengths[-1] * lengths[-2] * lengths[-3]

def part2(lines):
    return part1(lines, p2=True)


if __name__ == '__main__':

    part = 1
    expectedSampleResult = 40
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
