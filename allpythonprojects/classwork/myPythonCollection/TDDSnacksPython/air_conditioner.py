class AirConditioner:
    def __init__(self, is_on=True):
        self.switch_on_AC = is_on
        self.temperature = 16

    def switch_on_ac(self):
        if self.switch_on_AC:
            self.switch_on_AC = True
            return 'AC is turned on'

    def switch_off_ac(self):
        if not self.switch_on_AC:
            self.switch_on_AC = False
            return 'AC is turned off'

    def increase_temperature(self, increase):
        if increase:
                result = self.temperature + increase
                if result >= 16 or result <= 30:
                    return f'Temperature is increased to {result}'

    def decrease_temperature(self, decrease):
        if decrease:
            result = self.temperature - decrease
            return f'Temperature is decreased to {result}'

    def maximum_temperature(self, high_temperature):
        if high_temperature:
            result = self.temperature + high_temperature
            if result > 30:
                return f'Temperature is still 30'

    def minimum_temperature(self, low_temperature):
        if low_temperature:
            result = self.temperature - low_temperature
            if result < 16:
                return f'Temperature is still 16'

    def get_current_temperature(self):
        return self.temperature



