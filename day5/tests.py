import unittest

from common.common import read_input_lines
from impl import part1, part2


class AdventOfCodeTests(unittest.TestCase):

    def test_part1_sample(self):
        self.assertEqual(3, part1(read_input_lines("sample.txt")))

    def test_part1_input(self):
        self.assertEqual(567, part1(read_input_lines("input.txt")))

    def test_part2_sample(self):
        self.assertEqual(14, part2(read_input_lines("sample.txt")))

    def test_part2_input(self):
        p2 = part2(read_input_lines("input.txt"))
        if p2 <= 328457457331332:
            print("too low")
        if p2 >= 404771890356125:
            print("too high")
        self.assertEqual(4, p2)


if __name__ == '__main__':
    unittest.main()
