from enum import Enum


class Direction(Enum):
    UP = 'up'
    DOWN = 'down'
    FORWARD = 'forward'

    @classmethod
    def validate(cls, value):
        if value not in cls._value2member_map_:
            raise Exception('Invalid direction')
