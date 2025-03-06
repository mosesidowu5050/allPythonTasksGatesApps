import unittest
import semicolon_expense_tracker 


class TestExpenseTracker(unittest.TestCase):

    def test_validate_date(self):
	
        self.assertTrue(semicolon_expense_tracker.validate_date("06/03/2025"))
        self.assertFalse(semicolon_expense_tracker.validate_date("2025/03/06"))  
        self.assertFalse(semicolon_expense_tracker.validate_date("31/02/2025"))  

    def test_validate_description(self):
        self.assertTrue(semicolon_expense_tracker.validate_description("Groceries"))  
        self.assertFalse(semicolon_expense_tracker.validate_description(""))  
        self.assertFalse(semicolon_expense_tracker.validate_description("   "))  

    def test_validate_amount(self):
        self.assertTrue(semicolon_expense_tracker.validate_amount(10.5))  
        self.assertFalse(semicolon_expense_tracker.validate_amount(0.05)) 
        self.assertFalse(semicolon_expense_tracker.validate_amount(-5))  

    def test_total_amount(self):
        self.assertEqual(semicolon_expense_tracker.total_amount([10, 20, 30]), 60)  
        self.assertEqual(semicolon_expense_tracker.total_amount([0.1, 0.2, 0.3]), 0.6)
        self.assertEqual(semicolon_expense_tracker.total_amount([]), 0)  





#if __name__ == "__main__":
#    unittest.main()
