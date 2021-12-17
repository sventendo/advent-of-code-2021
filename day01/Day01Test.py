import unittest

from InputParser import InputParser
from Day01 import Day01


class Day01Test(unittest.TestCase):
    @staticmethod
    def test_part_1():
        parser = InputParser()
        values = parser.parse_int('input')
        day = Day01()
        increases = day.part1(values)
        print(increases)

    @staticmethod
    def test_part_2():
        parser = InputParser()
        values = parser.parse_int('input')
        day = Day01()
        increases = day.part2(values)
        print(increases)
