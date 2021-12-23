import unittest

from InputParser import InputParser
from day03.Day03 import Day03


class Day03Test(unittest.TestCase):
    @staticmethod
    def test_part_1():
        lines = InputParser.parse('input')
        print(Day03.part1(lines))

    @staticmethod
    def test_part_2():
        lines = InputParser.parse('input')
        print(Day03.part2(lines))