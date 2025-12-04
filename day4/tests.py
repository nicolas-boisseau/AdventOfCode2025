import unittest

from common.common import read_input_lines
from impl import part1, part2


class AdventOfCodeTests(unittest.TestCase):

    def test_part1_sample(self):
        self.assertEqual(13, part1(read_input_lines("sample.txt"))[0])

    def test_part1_input(self):
        self.assertEqual(1435, part1(read_input_lines("input.txt"))[0])

    def test_part2_sample(self):
        self.assertEqual(43, part2(read_input_lines("sample.txt")))

    def test_part2_input(self):
        self.assertEqual(8623, part2(read_input_lines("input.txt")))


if __name__ == '__main__':
    unittest.main()
