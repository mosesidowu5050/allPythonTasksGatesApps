from banke_account_app.banke_account import BankeAccount


class BankeAtmMachine:
    def __init__(self):
        self.accounts = []
        self.BankeAccount = BankeAccount("Lewis", "Thomas", "0204")

    def create_account(self, first_name, last_name, pin):
        if not first_name or not last_name or not pin:
            raise ValueError("Kindly fill the fields")
        account = BankeAccount(first_name, last_name, pin)
        self.accounts.append(account)
        return account

    def get_account(self):
        return self.accounts

    def get_account_size(self):
        return len(self.accounts)
    #
    # def transfer(self, pin, sender, receiver_pin, transfer_amount):
    #     if not pin or not sender or not receiver_pin or transfer_amount <= 0.0:
    #         raise ValueError("Invalid details")
    #     sender_account = self.find_account_by_the_pin(pin)
    #     receiver_account = self.find_account_by_the_pin(receiver_pin)
    #
    #     if sender_account is None or receiver_account is None:
    #         raise ValueError("Sender or Receiver account not found")
    #     sender_account.transfer(pin, receiver_account, transfer_amount)
    #     receiver_account.deposit(receiver_account.pin, transfer_amount)

    def get_balance(self, pin):
        if not pin:
            raise ValueError("PIN cannot be empty")
        account = self.find_account_by_the_pin(pin)
        if account is None:
            raise ValueError("Account not found")
        return account.get_balance()

    def close_account(self, pin, user_account):
        if not pin or not user_account:
            raise ValueError("Details cannot be empty")
        if isinstance(user_account, BankeAccount):
            user_account.withdraw(pin, user_account.get_balance(pin))
            self.accounts.remove(user_account)

    def deposit(self, pin, amount):
        if not pin or not amount:
            raise ValueError("Kindly fill the fields")
        account = self.find_account_by_the_pin(pin)
        if not account or account is None:
            raise ValueError("Account not found")
        account.deposit(pin, amount)


    def find_account_by_the_pin(self, pin):
        for account in self.accounts:
            if account.pin == pin:
                return account
        return None

    def find_account_by_user_name(self, user_name):
        for account in self.accounts:
            if f"{account.first_name} {account.last_name}" == user_name:
                return account
        return None


