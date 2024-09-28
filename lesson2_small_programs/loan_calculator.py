while True:
    # validate inputs
    def invalid_input(number_str):
        try:
            float(number_str)
        except ValueError:
            return True
        
        return False

    print("Welcome to Loan Calculator!")

    # get loan amount
    print("Please enter your LOAN AMOUNT: ")
    loan_amount = input()

    while invalid_input(loan_amount):
        print("Loan amount must be a number.")
        loan_amount = input()

    loan_amount = float(loan_amount)

    # get interest rate
    print("Please enter your ANNUAL PERCENTAGE RATE (APR): _% ")
    annual_percentage_rate = input()

    while invalid_input(annual_percentage_rate):
        print("Enter APR as a number, i.e. '5' for 5%.")
        annual_percentage_rate = input()
    
    annual_percentage_rate = float(annual_percentage_rate) / 100


    # calculate monthly interest from annual
    monthly_interest_rate = annual_percentage_rate / 12

    # get loan term
    print("Please enter your LOAN TERM in YEARS, MONTHS.")

    # get number of years
    print("YEARS: \n(Enter a whole number. If less than a year, enter 0).")
    loan_duration_years = input()

    def invalid_years_input(years_input):
        try: 
            int(years_input)
        except ValueError:
            return True

        return False

            
    while invalid_years_input(loan_duration_years):
        print("Loan duration YEARS must be a whole number.")
        loan_duration_years = input()

    loan_duration_years = float(loan_duration_years)    

    # get number of months
    print("MONTHS: ")
    loan_duration_months = input()

    while invalid_input(loan_duration_months):
        print("Loan duration MONTHS must be a number.")
        loan_duration_months = input()

    loan_duration_months = float(loan_duration_months)    

    # get total loan term in months
    loan_term = (loan_duration_years * 12) + loan_duration_months
    
    # calculate monthly payment
    def calculate(loan_amount, monthly_interest_rate, loan_term):
        try:
            monthly_payment = round(loan_amount * (monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-loan_term))), 2)
        except ZeroDivisionError:
            monthly_payment = round(loan_amount / loan_term, 2)

        return monthly_payment
    

    print(f"Your monthly payment is ${calculate(loan_amount, monthly_interest_rate, loan_term)}")

    # ask to continue
    print("Another calculation? Y / N")
    continue_choice = input()
    
    while continue_choice not in ['Yes', 'Y', 'y', 'No', 'N', 'n']:
        print("Please enter Y or N.")
        continue_choice = input()

    match continue_choice:
        case 'Y':
            continue
        case 'N':
            print("Thank you! Good luck with your loan.") 
            break
