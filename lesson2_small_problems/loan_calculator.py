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
    print("Please enter your ANNUAL PERCENTAGE RATE (APR): ___% ")
    annual_percentage_rate = input()

    while invalid_input(annual_percentage_rate):
        print("APR must be a number.")
        annual_percentage_rate = input()
    
    annual_percentage_rate = float(annual_percentage_rate)


    # calculate monthly interest from annual
    monthly_interest_rate = annual_percentage_rate / 12


    # determine loan period
    print("Is your loan duration represented in YEARS (Y) or MONTHS (M)? Years can be decimal.")
    loan_period = input()

    while loan_period not in ['Y', 'M']:
        print("Must respond with Y for years, M for months.")
        loan_period = input()


    # get loan duration
    print("Please enter your LOAN DURATION: ")
    loan_duration = input()

    while invalid_input(loan_duration):
        print("Loan duration must be a number.")
        loan_duration = input()

    loan_duration = float(loan_duration)    

    match loan_period:
        case 'Y':
            loan_duration_months = loan_duration * 12
        case 'M':
            loan_duration_months = loan_duration
 
            
    monthly_payment = loan_amount * (monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (- loan_duration_months)))
    rounded_monthly_payment = round(monthly_payment, 2)

    print(f"Your monthly payment is ${rounded_monthly_payment}")

    print("Another calculation? Y / N")
    continue_choice = input()
    
    while continue_choice not in ['Y', 'N']:
        print("Please enter Y or N.")
        continue_choice = input()

    match continue_choice:
        case 'Y':
            continue
        case 'N':
            print("Thank you! Good luck on your loan.") 
            break
