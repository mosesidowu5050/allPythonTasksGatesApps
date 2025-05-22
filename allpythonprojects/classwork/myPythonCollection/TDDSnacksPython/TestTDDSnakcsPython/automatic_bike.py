from idlelib.configdialog import changes


class AutomaticBike:
    def __init__(self, turned_on=True):
        self.switch_button = turned_on
        self.current_speed = 0
        self.current_gear = 1

    def turned_on_bike(self):
        if self.switch_button:
            return True

    def turned_off_bike(self):
        if self.switch_button:
            self.switch_button = False
            return False

    def change_gear(self, gear):
        if gear < 1 or gear > 4:
            return 'Gear must be between 1 and 4'
        else:
            self.current_gear = gear

    def accelerate(self):
        if self.current_gear == 1:
           self.current_speed += 1
        elif self.current_gear == 2:
           self.current_speed += 2
        elif self.current_gear == 3:
           self.current_speed += 3
        else:
           self.current_speed += 4
        self.update_speed()

    def get_current_speed(self):
        if self.switch_button:
            return self.current_speed

    def decelerate(self):
        if self.current_gear == 1:
            self.current_speed -= 1
        elif self.current_gear == 2:
            self.current_speed -= 2
        elif self.current_gear == 3:
            self.current_speed -= 3
        else:
            self.current_speed -= 4
        self.update_speed()

    def update_speed(self):
        if 0 >= self.current_speed <= 20:
            self.current_gear = 1
        elif 21 >= self.current_speed <= 30:
            self.current_gear = 2
        elif 30 >= self.current_speed <= 40:
            self.current_gear = 3
        else:
            self.current_gear = 4

    def get_current_gear(self):
        if self.current_gear:
            return self.current_gear






