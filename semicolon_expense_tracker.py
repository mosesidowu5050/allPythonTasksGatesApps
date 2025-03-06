from datetime import datetime



def print_menu():
    
    menu = """
    Welcome to Semicolon Expense Tracker App
    —------------------------------------------
    1. Add an expense
    2. View all expenses
    3. Calculate total expenses
    4. Exit

"""
    return print(menu)       
        
      
def validate_date(date):

     try:
        datetime.strptime(date, "%d/%m/%Y")
     
        return True

     except ValueError:

          return False


def validate_description(description):
    
    if description.strip():
       return True
    
    else:
        return False


def validate_amount(amount):
    
       if amount >= 0.1:
          return True

       else:
          return False

def total_amount(amount_taker)->float:
    total: float = 0;
    for counter in range(len(amount_taker)):
        total += amount_taker[counter]

    return round(total, 2)



def  main():
     date_taker = []
     description_taker = []
     amount_taker = []
     count = 0
     selection = 0

     while True:
           print_menu()
           try:  
              selection = int(input("Enter a selection from(1-4): "))
              if selection < 1 or selection > 4:
                 print("Please let your input be from range of 1 to 4")

           except ValueError:
                 print("Please only input an Integer")

           if selection == 1:
               count += 1
               while True:
                     date = input("\nEnter the expenses date in this format (DD/MM/YYYY): ")
                     if validate_date(date):
                      date_taker.append(date)
                      break
                     else:
                        print("Invalid date format, please enter date in the right format")

               while True:
                    description = input("Enter the description of your expenses: ")
                    if validate_description(description):
                       description_taker.append(description)
                       break  
                    else:
                      print("Your description cant be empty")

               while True:
                     try:
                        amount = float(input("Enter the expenses amount: "))
                        if validate_amount(amount):
                           amount_taker.append(amount)
                           break
                        else:
                            print("Your amount shouldnt be less than zero")

                     except ValueError:
                          print("Invalid Input, must be a number")

               print("\nExpenses added Successfully")

           elif selection == 2:
                print("\n EXPENSES  ")
                if count == 0:
                   print("No Expenses Yet........ select 1 to add expenses ")
                else:
                   for counter in range(len(date_taker)):
                       print(f"{counter + 1}. Date: {date_taker[counter]}, Description: {description_taker[counter]}, Amount: {amount_taker[counter]}")

           elif selection == 3:
                print(f"\nTotal Expenses:  {total_amount(amount_taker)}")
           elif selection == 4:
                print("\nExiting the app....Goodbye.")
                break







          
           

       



if __name__ == "__main__":
    main()











    


       
        