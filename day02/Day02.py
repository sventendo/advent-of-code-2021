from DayInterface import DayInterface
from day02.CommandFactory import CommandFactory
from day02.Navigation import Navigation
from day02.NavigationWithAim import NavigationWithAim


class Day02(DayInterface):
    @staticmethod
    def part1(values):
        navigation = Navigation()
        for command_string in values:
            navigation.follow_command(CommandFactory.from_string(command_string))
        return navigation.hash()

    @staticmethod
    def part2(values):
        navigation = NavigationWithAim()
        for command_string in values:
            navigation.follow_command(CommandFactory.from_string(command_string))
        return navigation.hash()
