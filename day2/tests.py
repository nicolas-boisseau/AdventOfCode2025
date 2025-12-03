import unittest

from common.common import read_input_lines
from impl import part1, part2


class AdventOfCodeTests(unittest.TestCase):

    def test_part1_sample(self):
        self.assertEqual(1227775554, part1(read_input_lines("sample.txt")))

    def test_part1_input(self):
        self.assertEqual(29940924880, part1(read_input_lines("input.txt")))

    def test_part2_sample(self):
        self.assertEqual(4174379265, part2(read_input_lines("sample.txt")))

    def test_part2_input(self):
        self.assertEqual(48631958998, part2(read_input_lines("input.txt")))


if __name__ == '__main__':
    unittest.main()
