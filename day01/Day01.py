from DayInterface import DayInterface
from Sonar import Sonar


class Day01(DayInterface):
    @staticmethod
    def part1(values):
        sonar = Sonar()
        sonar.count_increases(values)
        return sonar.increases

    @staticmethod
    def part2(values):
        sonar = Sonar()
        denoise_map = sonar.create_denoise_map(values)
        sonar.count_increases(denoise_map)
        return sonar.increases
