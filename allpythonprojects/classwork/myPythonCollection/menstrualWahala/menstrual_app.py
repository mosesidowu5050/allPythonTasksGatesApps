from datetime import timedelta


class MenstrualApp:
    def __init__(self, flow_start_date, flow_end_date, cycle_length):
        self.flow_start_date = flow_start_date
        self.flow_end_date = flow_end_date
        self.cycle_length = cycle_length
        self.flow_duration = 0

    def calculate_ovulation_period(self):
        return self.flow_end_date + timedelta(days=self.cycle_length // 2)

    def calculate_period_start_date(self):
        return self.flow_start_date

    def calculate_period_end_date(self):
        return self.flow_end_date

    def calculate_safe_period_after_flow_duration_start_date(self):
        return self.flow_end_date + timedelta(days= 1)

    def calculate_safe_period_end_date_after_flow_duration(self):
        return self.flow_end_date + timedelta(days= 6)

    def calculate_safe_period_end_date_before_next_period(self):
        return self.flow_end_date + timedelta(days = self.cycle_length - 1)

    def calculate_next_period_start_date(self):
        return self.flow_end_date + timedelta(days = self.cycle_length)
















