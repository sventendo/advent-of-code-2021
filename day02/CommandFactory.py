import re

from Command import Command
from day02.Direction import Direction


class CommandFactory:
    @staticmethod
    def from_string(string):
        pattern = re.compile(r'^(.+)\s(\d)$')
        matches = re.search(pattern, string)
        if matches:
            direction = matches.group(1)
            Direction.validate(direction)
            distance = int(matches.group(2))
            return Command(direction, distance)
        else:
            raise Exception
