import unittest

from myPythonCollection.TDDSnacksPython import air_conditioner


class MyTestCase(unittest.TestCase):
    def test_to_check_if_air_conditioner_is_on(self):
        new_AC = air_conditioner.AirConditioner(True)
        actual = new_AC.switch_on_ac()
        self.assertEqual(actual, 'AC is turned on')

    def test_to_check_if_air_conditioner_is_off(self):
        new_AC = air_conditioner.AirConditioner(False)
        actual = new_AC.switch_off_ac()
        self.assertEqual(actual, 'AC is turned off')

    def test_to_check_if_temperature_increase(self):
        new_AC = air_conditioner.AirConditioner(True)
        actual = new_AC.increase_temperature(2)
        self.assertEqual(actual, 'Temperature is increased to 18')

    # def test_to_check_if_temperature_decrease(self):
    #     new_AC = air_conditioner.AirConditioner(True)
    #     initial = new_AC.increase_temperature(4)
    #     actual = new_AC.decrease_temperature(1)
    #     self.assertEqual(initial, actual)

    def test_to_validate_the_maximum_temperature(self):
        new_AC = air_conditioner.AirConditioner(True)
        actual = new_AC.maximum_temperature(15)
        self.assertEqual(actual, 'Temperature is still 30')

    def test_to_validate_the_minimum_temperature(self):
        new_AC = air_conditioner.AirConditioner(True)
        actual = new_AC.minimum_temperature(1)
        expected = 'Temperature is still 16'
        self.assertEqual(actual, expected)

    def test_to_get_current_temperature(self):
        new_AC = air_conditioner.AirConditioner(True)
        # new_AC.increase_temperature(2)
        self.assertEqual(16, new_AC.get_current_temperature())



if __name__ == '__main__':
    unittest.main()
