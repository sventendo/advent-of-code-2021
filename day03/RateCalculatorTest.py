import unittest

from InputParser import InputParser
from day03.RateCalculator import RateCalculator


class RateCalculatorTest(unittest.TestCase):
    def test_example_lines(self):
        rate_calculator = RateCalculator(5)
        line = '01100'
        self.assertEqual(0, rate_calculator.parse_line(line, 0))
        self.assertEqual(0, rate_calculator.parse_line(line, 1))
        self.assertEqual(1, rate_calculator.parse_line(line, 2))
        self.assertEqual(1, rate_calculator.parse_line(line, 3))
        self.assertEqual(0, rate_calculator.parse_line(line, 4))

    def test_example_rate_at_column(self):
        rate_calculator = RateCalculator(5)
        lines = InputParser.parse('example')
        self.assertEqual(0, rate_calculator.get_gamma_rate_at_column(lines, 0))
        self.assertEqual(1, rate_calculator.get_gamma_rate_at_column(lines, 1))

    def test_example_rate(self):
        rate_calculator = RateCalculator(5)
        lines = InputParser.parse('example')
        self.assertEqual(22, rate_calculator.get_gamma_rate(lines))

    def test_gamma_to_epsilon(self):
        rate_calculator = RateCalculator(5)
        self.assertEqual(9, rate_calculator.gamma_to_epsilon(22))

    def test_power_consumption(self):
        rate_calculator = RateCalculator(5)
        lines = InputParser.parse('example')
        self.assertEqual(198, rate_calculator.get_power_consumption(lines))

    def test_value_at_column(self):
        rate_calculator = RateCalculator(3)
        self.assertTrue(rate_calculator.line_has_value_at_column('011', 0, 1))
        self.assertTrue(rate_calculator.line_has_value_at_column('011', 1, 1))
        self.assertFalse(rate_calculator.line_has_value_at_column('011', 2, 1))

    def test_filter_value_at_column(self):
        rate_calculator = RateCalculator(3)
        lines = rate_calculator.filter_lines_by_column_value(['011', '110', '111'], 2, 1)
        self.assertEqual(2, len(lines))
        self.assertIn('110', lines)
        self.assertIn('111', lines)

    def test_get_oxygen_generator_rating(self):
        rate_calculator = RateCalculator(5)
        lines = InputParser.parse('example')
        self.assertEqual(23, rate_calculator.get_oxygen_generator_rating(lines))

    def test_get_carbon_scrubber_rating(self):
        rate_calculator = RateCalculator(5)
        lines = InputParser.parse('example')
        self.assertEqual(10, rate_calculator.get_carbon_scrubber_rating(lines))
