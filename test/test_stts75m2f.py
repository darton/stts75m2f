import unittest
from stts75m2f import STTS75M2F

class TestSTTS75M2F(unittest.TestCase):
    def test_read_temperature(self):
        sensor = STTS75M2F()
        temperature = sensor.read_temperature()
        self.assertIsInstance(temperature, float)

if __name__ == '__main__':
    unittest.main()
