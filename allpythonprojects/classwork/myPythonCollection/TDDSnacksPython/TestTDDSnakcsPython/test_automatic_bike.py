import unittest

from myPythonCollection.TDDSnacksPython.TestTDDSnakcsPython import automatic_bike
from myPythonCollection.TDDSnacksPython.TestTDDSnakcsPython.automatic_bike import AutomaticBike


class MyTestCase(unittest.TestCase):
    def test_if_bike_is_turned_on(self):
        new_bike = automatic_bike.AutomaticBike(True)
        self.assertTrue(new_bike.turned_on_bike())

    def test_if_bike_is_turned_off(self):
        new_bike = automatic_bike.AutomaticBike(True)
        self.assertFalse(new_bike.turned_off_bike())

    def test_to_validate_if_the_gear_less_than_one(self):
        new_bike = automatic_bike.AutomaticBike(True)
        actual = new_bike.change_gear(0)
        self.assertEqual('Gear must be between 1 and 4', actual)

    def test_to_validate_if_the_gear_greater_than_four(self):
        new_bike = automatic_bike.AutomaticBike(True)
        actual = new_bike.change_gear(8)
        self.assertEqual('Gear must be between 1 and 4', actual)

    def test_to_check_bike_accelerate_on_gear_one(self):
        new_bike = automatic_bike.AutomaticBike(True)
        new_bike.change_gear(1)
        new_bike.accelerate()
        self.assertEqual(1, new_bike.get_current_speed())

    def test_to_check_bike_accelerate_on_gear_two(self):
        new_bike = automatic_bike.AutomaticBike(True)
        new_bike.change_gear(2)
        new_bike.accelerate()
        self.assertEqual(2, new_bike.get_current_speed())

    def test_to_check_bike_accelerate_on_gear_three(self):
        new_bike = automatic_bike.AutomaticBike(True)
        new_bike.change_gear(3)
        new_bike.accelerate()
        self.assertEqual(3, new_bike.get_current_speed())

    def test_to_check_bike_accelerate_on_gear_four(self):
        new_bike = automatic_bike.AutomaticBike(True)
        new_bike.change_gear(4)
        new_bike.accelerate()
        self.assertEqual(4, new_bike.get_current_speed())

    def test_that_get_update_of_current_speed(self):
        new_bike = automatic_bike.AutomaticBike(True)
        new_bike.change_gear(1)
        new_bike.accelerate()
        new_bike.change_gear(1)
        new_bike.accelerate()
        self.assertEqual(2, new_bike.get_current_speed())

    def test_that_check_bike_decelerate(self):
        new_bike = automatic_bike.AutomaticBike(True)
        new_bike.change_gear(1)
        new_bike.accelerate()
        new_bike.accelerate()
        new_bike.decelerate()
        self.assertEqual(1, new_bike.get_current_speed())

    def test_that_bike_decelerate_on_gear_two(self):
        new_bike = automatic_bike.AutomaticBike(True)
        new_bike.change_gear(2)
        new_bike.accelerate()
        new_bike.accelerate()
        new_bike.decelerate()
        self.assertEqual(2, new_bike.get_current_speed())

    def test_that_bike_decelerate_on_gear_three(self):
        new_bike = automatic_bike.AutomaticBike(True)
        new_bike.change_gear(3)
        new_bike.accelerate()
        new_bike.accelerate()
        new_bike.decelerate()
        self.assertEqual(3, new_bike.get_current_speed())

    def test_that_check_bike_decelerate_in_gear_four(self):
        new_bike = automatic_bike.AutomaticBike(True)
        new_bike.change_gear(4)
        new_bike.accelerate()
        new_bike.accelerate()
        new_bike.decelerate()
        self.assertEqual(4, new_bike.get_current_speed())

    def test_gear_one_change_automatically_to_gear_two(self):
        new_bike = automatic_bike.AutomaticBike(True)
        for speed in range(21):
            new_bike.change_gear(1)
            new_bike.accelerate()
            self.assertEqual(2, new_bike.get_current_gear())

    def test_gear_two_change_automatically_to_gear_three(self):
        new_bike = automatic_bike.AutomaticBike(True)
        for speed1 in range(20):
            new_bike.change_gear(1)
            new_bike.accelerate()
        for speed2 in range(10):
            new_bike.change_gear(2)
            new_bike.accelerate() 
            self.assertEqual(3, new_bike.get_current_gear())

    # def test_gear_three_change_automatically_to_gear_four(self):
    #     new_bike = automatic_bike.AutomaticBike(True)
    #     new_bike.change_gear(3)
    #     for speed in range(40):
    #         new_bike.accelerate()
    #     self.assertEqual(4, new_bike.get_current_gear())
    #



if __name__ == '__main__':
    unittest.main()
