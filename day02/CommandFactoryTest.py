import unittest

from day02.CommandFactory import CommandFactory
from day02.Direction import Direction


class MyTestCase(unittest.TestCase):
    def test_command_parsing(self):
        command_factory = CommandFactory()
        command = command_factory.from_string('forward 2')
        self.assertEqual(2, command.distance)
        self.assertEqual(Direction.FORWARD.value, command.direction)

        self.assertRaises(Exception, command_factory.from_string, 'backward 2')
