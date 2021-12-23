class RateCalculator:
    def __init__(self, length):
        self.length = length

    # columns are 0-based, right to left
    @staticmethod
    def parse_line(line, column):
        filter_bit = 2 ** column
        return (int(line, 2) & filter_bit) >> column

    def get_gamma_rate_at_column(self, lines, column):
        count = len(lines)
        value_sum = 0
        for line in lines:
            value_sum += self.parse_line(line, column)
        return (0, 1)[value_sum >= count / 2]

    def get_epsilon_rate_at_column(self, lines, column):
        return self.get_gamma_rate_at_column(lines, column) ^ 1

    def get_rate_at_column(self, lines, column, check_value):
        count = len(lines)
        value_sum = 0
        for line in lines:
            value_sum += self.parse_line(line, column)
        return (1, 0)[value_sum >= count / 2] ^ check_value

    def get_gamma_rate(self, lines):
        value_sum = 0
        for column in range(0, self.length):
            value_sum += 2 ** column * self.get_gamma_rate_at_column(lines, column)
        return value_sum

    def gamma_to_epsilon(self, gamma):
        return (1 << self.length) - gamma - 1

    def get_power_consumption(self, lines):
        gamma_rate = self.get_gamma_rate(lines)
        return gamma_rate * self.gamma_to_epsilon(gamma_rate)

    def get_oxygen_generator_rating(self, lines):
        return self.get_rating(lines, 1)

    def get_carbon_scrubber_rating(self, lines):
        return self.get_rating(lines, 0)

    def get_rating(self, lines, check_value):
        column = self.length - 1
        while len(lines) > 1 and column >= 0:
            gamma_rate = self.get_rate_at_column(lines, column, check_value)
            lines = self.filter_lines_by_column_value(lines, column, gamma_rate)
            column -= 1

        if len(lines) == 1:
            return int(lines[0], 2)

        raise Exception('No oxygen rating found.')

    def filter_lines_by_column_value(self, lines, column, value):
        return list(filter(lambda line: self.line_has_value_at_column(line, column, value), lines))

    @staticmethod
    def line_has_value_at_column(line, column, value):
        return ((1 << column) & int(line, 2)) >> column == value

    def get_life_support_rating(self, lines):
        return self.get_oxygen_generator_rating(lines) * self.get_carbon_scrubber_rating(lines)
