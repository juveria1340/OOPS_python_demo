import unittest
from car import Car


class TestCar(unittest.TestCase):
    def setUp(self):
        self.car = Car('Toyota', 'Camry', 2020)

    def test_get_descriptive_name(self):
        self.assertEqual(self.car.get_descriptive_name(), '2020 Toyota Camry')

    def test_read_odometer(self):
        self.assertEqual(self.car.read_odometer(), 'This car has 0 miles on it.')

    def test_update_odometer(self):
        self.car.update_odometer(100)
        self.assertEqual(self.car.odometer_reading, 100)

    def test_increment_odometer(self):
        self.car.increment_odometer(50)
        self.assertEqual(self.car.odometer_reading, 50)


if __name__ == '__main__':
    unittest.main()
