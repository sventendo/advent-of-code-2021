import unittest

from InputParser import InputParser
from day02.Command import Command
from day02.CommandFactory import CommandFactory
from day02.Direction import Direction
from day02.Navigation import Navigation


class NavigationTest(unittest.TestCase):
    def test_single_commands(self):
        navigation = Navigation()
        navigation.follow_command(Command(Direction.FORWARD.value, 5))
        navigation.follow_command(Command(Direction.DOWN.value, 3))
        navigation.follow_command(Command(Direction.UP.value, 1))
        self.assertEqual(5, navigation.x)
        self.assertEqual(2, navigation.depth)

    def test_example_input(self):
        command_strings = InputParser.parse('example')
        navigation = Navigation()
        for command_string in command_strings:
            navigation.follow_command(CommandFactory.from_string(command_string))
        self.assertEqual(15, navigation.x)
        self.assertEqual(10, navigation.depth)
        self.assertEqual(150, navigation.hash())
