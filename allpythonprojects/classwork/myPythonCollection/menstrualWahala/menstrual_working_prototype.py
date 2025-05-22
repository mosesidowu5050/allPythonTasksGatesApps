from datetime import datetime
from menstrual_app import MenstrualApp

def main():
    print("Welcome to Menstrual Wahala!")

    try:
        flow_start_date_input = input("Enter your flow start date (YYYY-MM-DD): ")
        flow_end_date_input = input("Enter your flow end date (YYYY-MM-DD): ")
        cycle_length_input = input("Enter your cycle length in days: ")

        try:
            flow_start_date = datetime.strptime(flow_start_date_input, "%Y-%m-%d").date()
            flow_end_date = datetime.strptime(flow_end_date_input, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("The date format must be YYYY-MM-DD. Enter valid dates.")

        try:
            cycle_length = int(cycle_length_input)
            if cycle_length <= 0:
                raise ValueError("Invalid positive cycle length.")
            if cycle_length < 21 or cycle_length > 35:
                raise ValueError("Irregular cycle length. Kindly see the doctor.")
        except ValueError:
            raise ValueError("Invalid cycle length.")

        if flow_start_date >= flow_end_date:
            raise ValueError("The flow start date must be earlier than the flow end date.")


        menstrual_app = MenstrualApp(flow_start_date, flow_end_date, cycle_length)

        print("Menstrual Information: ")
        print(f"Flow Start Date: {menstrual_app.flow_start_date}")
        print(f"Flow End Date: {menstrual_app.flow_end_date}")
        print(f"Cycle Length: {menstrual_app.cycle_length} days")
        print(f"Ovulation Date: {menstrual_app.calculate_ovulation_period()}")
        print(f"Safe Period Start After Flow: {menstrual_app.calculate_safe_period_after_flow_duration_start_date()}")
        print(f"Safe Period End After Flow: {menstrual_app.calculate_safe_period_end_date_after_flow_duration()}")
        print(f"Safe Period End Before Next Period: {menstrual_app.calculate_safe_period_end_date_before_next_period()}")
        print(f"Next Period Start Date: {menstrual_app.calculate_next_period_start_date()}")

    except ValueError as e:
        print(f"Invalid details: {e}")




if __name__ == "__main__":
    main()