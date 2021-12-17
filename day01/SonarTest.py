import unittest

from InputParser import InputParser
from Sonar import Sonar


class SonarTest(unittest.TestCase):
    def test_count_increases(self):
        parser = InputParser()
        values = parser.parse_int('example')
        sonar = Sonar()
        sonar.count_increases(values)
        self.assertEqual(7, sonar.increases)

    def test_denoise_map(self):
        sonar = Sonar()
        self.assertListEqual([6, 15], sonar.create_denoise_map([1, 2, 3, 10]))
