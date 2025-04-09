from TDDSnacksPython.air_conditioner import AirConditioner


class BankeAccount:
    def __init__(self, first_name, last_name, pin):
        if not first_name or not last_name or not pin:
            raise ValueError("Bank Account must have fields")
        if len(pin) != 4 or not pin.isdigit():
            raise ValueError("Pin must be 4 digits")
        self.first_name = first_name
        self.last_name = last_name
        self.pin = pin
        self.balance = 0.0

    def get_balance(self):
        return self.balance

    def get_name(self):
        return f"{self.first_name} {self.last_name}"

    def deposit(self, pin, deposit_amount):
        if pin != self.pin:
            raise ValueError("Invalid PIN")
        if deposit_amount <= 0.0:
            raise ValueError("Invalid deposit amount")

        self.balance += deposit_amount

    def withdraw(self, pin, withdraw_amount):
        if pin != self.pin:
            raise ValueError("Invalid PIN")
        if withdraw_amount <= 0.0:
            raise ValueError("Invalid withdraw amount")
        if withdraw_amount > self.balance:
            raise ValueError("Insufficient balance")

        self.balance -= withdraw_amount

    def transfer(self, pin, receiver, transfer_amount):
        if transfer_amount <= 0.0:
            raise ValueError("Invalid transfer amount")
        if pin != self.pin:
            raise ValueError("PIN must be 4 digits")
        if not isinstance(receiver, BankeAccount):
            raise ValueError("Invalid transfer amount")

        self.withdraw(pin, transfer_amount)
        receiver.deposit(receiver.pin, transfer_amount)

    def change_pin(self, old_pin, new_pin):
        if old_pin != self.pin:
            raise ValueError("Invalid PIN")
        if len(old_pin) != 4 or not old_pin.isdigit():
            raise ValueError("PIN must be 4 digits")
        if old_pin == self.pin:
            self.pin = new_pin






