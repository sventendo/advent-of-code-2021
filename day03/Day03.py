from DayInterface import DayInterface
from day03.RateCalculator import RateCalculator


class Day03(DayInterface):
    @staticmethod
    def part1(lines):
        length = len(lines[0])
        rate_calculator = RateCalculator(length)
        return rate_calculator.get_power_consumption(lines)

    @staticmethod
    def part2(lines):
        length = len(lines[0])
        rate_calculator = RateCalculator(length)
        return rate_calculator.get_life_support_rating(lines)
