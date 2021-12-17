class Sonar:
    def __init__(self):
        self.increases = 0
        self.current_value = 0

    def count_increases(self, values):
        self.increases = 0
        self.current_value = values.pop(0)
        for value in values:
            if value > self.current_value:
                self.increases += 1
            self.current_value = value

    @staticmethod
    def create_denoise_map(values):
        denoise_map = []
        for index in range(len(values) - 2):
            denoise_map.append(sum(values[index:index + 3]))

        return denoise_map
