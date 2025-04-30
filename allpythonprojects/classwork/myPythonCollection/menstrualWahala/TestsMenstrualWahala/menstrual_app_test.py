import unittest
from datetime import datetime, timedelta


from menstrualWahala import menstrual_app


class MyTestCase(unittest.TestCase):
    def test_that_calculate_ovulation_period_is_valid(self):
        cycle_length = 28
        flow_start_date = datetime(2020, 5, 5).date()
        flow_end_date = datetime(2020, 1, 10).date()

        menstrual = menstrual_app.MenstrualApp(flow_start_date, flow_end_date, cycle_length)
        actual_ovulation_date = menstrual.calculate_ovulation_period()
        expected_ovulation_date = flow_end_date + timedelta(days=cycle_length // 2)
        self.assertEqual(actual_ovulation_date, expected_ovulation_date)

    def test_period_start_date_is_valid(self):
        cycle_length = 28
        flow_start_date = datetime(2020, 5, 5).date()
        flow_end_date = datetime(2020, 1, 10).date()

        menstrual = menstrual_app.MenstrualApp(flow_start_date, flow_end_date, cycle_length)

        actual_start_date = menstrual.calculate_period_start_date()
        self.assertEqual(actual_start_date, flow_start_date)

    def test_period_end_date_is_valid(self):
        cycle_length = 28
        flow_start_date = datetime(2020, 5, 5).date()
        flow_end_date = datetime(2020, 1, 10).date()

        menstrual = menstrual_app.MenstrualApp(flow_start_date, flow_end_date, cycle_length)
        expected_end_date = menstrual.calculate_period_end_date()
        self.assertEqual(expected_end_date, flow_end_date)

    def test_that_checks_if_safe_periods_start_date_is_valid(self):
        cycle_length = 28
        flow_start_date = datetime(2020, 5, 5).date()
        flow_end_date = datetime(2020, 1, 10).date()

        menstrual = menstrual_app.MenstrualApp(flow_start_date, flow_end_date, cycle_length)
        actual_safe_period = menstrual.calculate_safe_period_after_flow_duration_start_date()
        expected_safe_period = flow_end_date + timedelta(days= 1)
        self.assertEqual(actual_safe_period, expected_safe_period)

    def test_safe_periods_after_flow_duration(self):
        cycle_length = 28
        flow_start_date = datetime(2020, 5, 5).date()
        flow_end_date = datetime(2020, 1, 10).date()

        menstrual = menstrual_app.MenstrualApp(flow_start_date, flow_end_date, cycle_length)
        actual_safe_period_date = menstrual.calculate_safe_period_end_date_after_flow_duration()
        expected_safe_period_end_date = flow_end_date + timedelta(days= 6)
        self.assertEqual(actual_safe_period_date, expected_safe_period_end_date)

    def test_safe_period_end_date_before_next_period(self):
        cycle_length = 28
        flow_start_date = datetime(2020, 5, 5).date()
        flow_end_date = datetime(2020, 1, 10).date()

        menstrual = menstrual_app.MenstrualApp(flow_start_date, flow_end_date, cycle_length)
        actual_safe_period_date = menstrual.calculate_safe_period_end_date_before_next_period()
        expected_safe_period_end_date = flow_end_date + timedelta(days=cycle_length - 1)
        self.assertEqual(actual_safe_period_date, expected_safe_period_end_date)


    def test_that_calculate_next_period_start_date(self):
        cycle_length = 28
        flow_start_date = datetime(2020, 5, 5).date()
        flow_end_date = datetime(2020, 1, 10).date()

        menstrual = menstrual_app.MenstrualApp(flow_start_date, flow_end_date, cycle_length)
        actual_next_period_start_date = menstrual.calculate_next_period_start_date()
        expected_next_period_start_date = flow_end_date + timedelta(days = cycle_length)
        self.assertEqual(actual_next_period_start_date, expected_next_period_start_date)





if __name__ == '__main__':
    unittest.main()
