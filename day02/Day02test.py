import unittest

from InputParser import InputParser
from day02.Day02 import Day02


class Day02Test(unittest.TestCase):
    @staticmethod
    def test_part_1():
        command_strings = InputParser.parse('input')
        day = Day02()
        print(day.part1(command_strings))

    @staticmethod
    def test_part_2():
        command_strings = InputParser.parse('input')
        day = Day02()
        print(day.part2(command_strings))
