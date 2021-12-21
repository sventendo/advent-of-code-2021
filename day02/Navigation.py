from day02.Direction import Direction


class Navigation:
    def __init__(self):
        self.x = 0
        self.depth = 0

    def follow_command(self, command):
        if command.direction == Direction.FORWARD.value:
            self.x += command.distance
        elif command.direction == Direction.UP.value:
            self.depth -= command.distance
        elif command.direction == Direction.DOWN.value:
            self.depth += command.distance

    def hash(self):
        return self.x * self.depth
