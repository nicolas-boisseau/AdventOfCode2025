import os.path
from collections import defaultdict

from common.common import download_input_if_not_exists, post_answer, capture, capture_all, read_input_lines
from day11.Graph import Graph

download_input_if_not_exists(2025)

def extract_and_build_directed_graph(lines) -> Graph:
    devices = defaultdict(list)
    for l in lines:
        split = l.split(": ")
        id = split[0]
        outputs = split[1].split(" ")
        devices[id] = outputs

    g = Graph()
    for id, outputs in devices.items():
        # print(f"Device {id} has outputs {outputs}")
        for o in outputs:
            g.add_edge(id, o, 1)
    return g

def part1(lines):
    g = extract_and_build_directed_graph(lines)

    paths = g.find_all_paths("you", "out")

    return len(paths)

def part2(lines):
    g = extract_and_build_directed_graph(lines)

    paths_svr_dac = g.find_all_paths("svr", "dac")
    print(f"Found {len(paths_svr_dac)} paths from svr to dac")

    paths_svr_fft = g.find_all_paths("svr", "fft")
    print(f"Found {len(paths_svr_fft)} paths from svr to fft")

    paths_dac_fft = g.find_all_paths("dac", "fft")
    print(f"Found {len(paths_dac_fft)} paths from dac to fft")

    paths_fft_dac = g.find_all_paths("fft", "dac")
    print(f"Found {len(paths_fft_dac)} paths from fft to dac")

    paths_fft_out = g.find_all_paths("fft", "out")
    print(f"Found {len(paths_fft_out)} paths from fft to out")

    paths_dac_out = g.find_all_paths("dac", "out")
    print(f"Found {len(paths_dac_out)} paths from dac to out")


    return -1


if __name__ == '__main__':

    part = 1
    expectedSampleResult = 5
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
