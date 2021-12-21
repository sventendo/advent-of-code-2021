import unittest

from InputParser import InputParser
from day02.CommandFactory import CommandFactory
from day02.NavigationWithAim import NavigationWithAim


class NavigationTest(unittest.TestCase):
    def test_example_input(self):
        command_strings = InputParser.parse('example')
        navigation = NavigationWithAim()
        for command_string in command_strings:
            navigation.follow_command(CommandFactory.from_string(command_string))
        self.assertEqual(15, navigation.x)
        self.assertEqual(60, navigation.depth)
        self.assertEqual(900, navigation.hash())
