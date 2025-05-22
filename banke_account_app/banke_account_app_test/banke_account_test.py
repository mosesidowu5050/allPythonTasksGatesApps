import unittest

from banke_account_app import banke_account, banke_atm_machine
from banke_account_app.banke_account import BankeAccount
from banke_account_app.banke_atm_machine import BankeAtmMachine


class MyTestCase(unittest.TestCase):
    def test_if_amount_is_zero(self):
        account = banke_account.BankeAccount("Dayo", "Lawal", "0202")
        self.assertEqual(0.0, account.get_balance())

    def test_if_details_is_empty(self):
        with self.assertRaises(ValueError):
            account = BankeAccount("", "", "")

    def test_raise_exception_when_first_name_is_empty(self):
        with self.assertRaises(ValueError):
            account = BankeAccount("", "Lawal", "0202")

    def test_raise_exception_when_length_of_pin_exceeds_four_and_contains_letters(self):
        with self.assertRaises(ValueError):
            account = BankeAccount("Dayo", "Lawal", "020245")
            account = BankeAccount("Dayo", "Lawal", "02PT")

    def test_raise_exception_when_last_name_is_empty(self):
        with self.assertRaises(ValueError):
            account = BankeAccount("Dayo", "", "0202")

    def test_raise_exception_when_pin_is_empty(self):
        with self.assertRaises(ValueError):
            account = BankeAccount("Dayo", "Lawal", "")

    def test_if_get_name_works_properly(self):
        account = BankeAccount("Dayo", "Lawal", "0202")
        self.assertEqual(account.get_name(), "Dayo Lawal")

    def test_that_check_if_deposit_works_properly(self):
        account = BankeAccount("Dayo", "Lawal", "0202")
        account.deposit("0202", 1000.00)
        self.assertEqual(account.get_balance(), 1000.00)

    def test_that_throws_exception_when_pin_is_invalid(self):
        with self.assertRaises(ValueError):
            account = BankeAccount("Dayo", "Lawal", "0202")
            account.deposit("1122", 1000.00)
            account = BankeAccount("Dayo", "Lawal", "02923")
            account = BankeAccount("Dayo", "Lawal", "7TY2")

    def test_that_throws_exception_when_deposit_amount_is_negative(self):
        with self.assertRaises(ValueError):
            account = BankeAccount("Dayo", "Lawal", "0202")
            account.deposit("0202", -1000.00)

    def test_that_throws_exception_when_deposit_amount_is_zero(self):
        with self.assertRaises(ValueError):
            account = BankeAccount("Dayo", "Lawal", "0202")
            account.deposit("0202", 0.0)

    def test_that_checks_withdraw_works_properly(self):
        account = BankeAccount("Dayo", "Lawal", "0202")
        account.deposit("0202", 1000.00)
        account.withdraw("0202", 500.00)
        self.assertEqual(account.get_balance(), 500.00)


    def test_that_throw_exception_if_withdrawal_pin_is_invalid(self):
        with self.assertRaises(ValueError):
            account = BankeAccount("Dayo", "Lawal", "0202")
            account.withdraw("6202", 1000.00)
            account = BankeAccount("Dayo", "Lawal", "02923")
            account = BankeAccount("Dayo", "Lawal", "7TY2")

    def test_that_checks_if_withdrawal_amount_is_negative(self):
        with self.assertRaises(ValueError):
            account = BankeAccount("Dayo", "Lawal", "0202")
            account.withdraw("0202", -500.00)

    def test_that_throw_exception_if_withdrawal_amount_is_zero(self):
        with self.assertRaises(ValueError):
            account = BankeAccount("Dayo", "Lawal", "0202")
            account.withdraw("0202", 0.0)

    def test_that_throws_exception_when_withdrawal_amount_greater_than_balance(self):
        with self.assertRaises(ValueError):
            account = BankeAccount("Dayo", "Lawal", "0202")
            account.deposit("0202", 1000.00)
            account.withdraw("0202", 1100.00)

    def test_that_checks_if_transfer_works_properly(self):
        dayo = BankeAccount("Dayo", "Lawal", "0202")
        bode = BankeAccount("Bode", "Oderinde", "9230")
        dayo.deposit("0202", 1000.00)
        dayo.transfer("0202", bode, 500.00)
        self.assertEqual(dayo.get_balance(), 500.00)
        self.assertEqual(bode.get_balance(), 500.00)

    def test_throws_exception_when_withdrawal_pin_is_invalid(self):
        with self.assertRaises(ValueError):
            account = BankeAccount("Dayo", "Lawal", "0202")
            account.transfer("02YE", "Ayo", 1000.00)

    def test_if_list_is_empty(self):
        atm = BankeAtmMachine()
        self.assertEqual(atm.get_account_size(), 0)

    def test_to_check_the_length_of_two_account(self):
        atm = BankeAtmMachine()
        atm.create_account("Dayo", "Lawal", "0202")
        atm.create_account("Ayo", "Lawson", "9239")
        self.assertEqual(atm.get_account_size(), 2)

    def test_that_checks_if_account_can_be_access_by_index_number(self):
        atm = BankeAtmMachine()
        atm.create_account("Dayo", "Lawal", "0202")
        atm.create_account("Ayo", "Lawson", "9239")
        self.assertEqual(atm.get_account()[0].first_name,  "Dayo")
        self.assertEqual(atm.get_account()[1].first_name, "Ayo")

    def test_checks_if_transfer_works_properly(self):
        atm = BankeAtmMachine()
        dayo = atm.create_account("Dayo", "Lawal", "0202")
        ayo = atm.create_account("Ayo", "Lawson", "9239")
        dayo.deposit("0202", 1000.00)
        atm.transfer("0202", dayo, ayo, 500.00)
        self.assertEqual(dayo.get_balance(), 500.00)
        self.assertEqual(ayo.get_balance(), 500.00)

    def test_throws_exception_when_transfer_details_is_invalid(self):
        with self.assertRaises(ValueError):
            atm = BankeAtmMachine()
            dayo = atm.create_account("Dayo", "Lawal", "0202")
            ayo = atm.create_account("Ayo", "Lawson", "9239")
            dayo.deposit("0202", 1000.00)
            atm.transfer("", None, None, 500.00)

    def test_that_get_balance_works_properly(self):
        atm = BankeAtmMachine()
        dayo = atm.create_account("Dayo", "Lawal", "0202")
        bode = atm.create_account("Bode", "Oderinde", "9230")
        dayo.deposit("0202", 1000.00)
        bode.deposit("9230", 950.00)
        self.assertEqual(atm.get_balance("0202", dayo), 1000.00)
        self.assertEqual(atm.get_balance("9230", bode), 950.00)

    def test_throws_exceptions_if_get_balance_details_not_valid(self):
        with self.assertRaises(ValueError):
            atm = BankeAtmMachine()
            dayo = atm.create_account("Dayo", "Lawal", "0202")
            ayo = atm.create_account("Ayo", "Lawson", "9239")
            dayo.deposit("0202", 1000.00)
            ayo.deposit("9230", 950.00)

            self.assertEqual(atm.get_balance("0202", None), 1000.00)
            self.assertEqual(atm.get_balance(None, None), 950.00)

    def test_to_confirm_account_is_deactivated(self):
        atm = BankeAtmMachine()
        bode = atm.create_account("Bode", "Oderinde", "9230")
        dayo = atm.create_account("Dayo", "Lawal", "0202")
        bode.deposit("9230", 1000.00)
        atm.close_account("9230", bode)
        self.assertEqual(atm.get_account_size(), 1)

    def test_that_throws_exception_when_account_details_is_not_valid(self):
        with self.assertRaises(ValueError):
            atm = BankeAtmMachine()
            dayo = atm.create_account("Dayo", "Lawal", "0202")
            dayo.deposit("0202", 1000.00)
            atm.close_account(None, None)
        
    def test_that_change_pin_works_perfectly(self):
        bode = BankeAccount("Bode", "Thomas", "0204")
        bode.change_pin("0204", "0001")
        bode.deposit("0001", 1000.00)

        self.assertEqual(bode.get_balance(), 1000.00)

    def test_throw_exception_when_change_pin_is_invalid(self):
        with self.assertRaises(ValueError):
            bode = BankeAccount("Wale", "Lewis", "0204")
            bode.change_pin("0104", "0001")
            bode.change_pin("234", "0001")
            bode.change_pin("TY33", "0001")



if __name__ == '__main__':
    unittest.main()
