from day02.Direction import Direction


class NavigationWithAim:
    def __init__(self):
        self.x = 0
        self.depth = 0
        self.aim = 0

    def follow_command(self, command):
        if command.direction == Direction.FORWARD.value:
            self.x += command.distance
            self.depth -= self.aim * command.distance
        elif command.direction == Direction.UP.value:
            self.aim += command.distance
        elif command.direction == Direction.DOWN.value:
            self.aim -= command.distance

    def hash(self):
        return self.x * self.depth
