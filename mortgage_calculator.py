def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try: 
        number = float(number_str)
        if number <= 0:
            raise ValueError(f"Value must be > 0: {number_str}")
    except ValueError:
        return True
    return False


prompt("Welcome to Mortgage Calculator")

while True:
    prompt("What's the amount of your loan?")

    get_amount = input()
    while invalid_number(get_amount):
        prompt("Please enter a positive number")
        get_amount = input()

    prompt("What's your Annual Percentage Rate (APR)?")
    prompt("(Example: 5 for 5% or 2.5 for 2.5%)")
    
    get_apr = input() 

    while invalid_number(get_apr):
        prompt("Please enter a positive number")
        get_apr = input()

    prompt("What's your loan duration (in years)?")
    get_duration_years = input()

    while invalid_number(get_duration_years):
        prompt("Please enter a positive number")
        get_duration_years = input()

    annual_interest_rate = float(get_duration_years) / 100
    monthly_interest_rate = annual_interest_rate / 12
    months = float(get_duration_years) * 12
    loan_amount = float(get_amount)

    monthly_payment = loan_amount * (
        monthly_interest_rate / 
        (1 - (1 + monthly_interest_rate) ** (-months))
    )

    prompt(f'Your monthly payment is: ${monthly_payment: .2f}')

    prompt("Do you want to calculate another loan?")
    answer = input().lower()
    while True:
        if answer.startswith('n') or answer.startswith('y'):
            break

        prompt('Please enter "yes" or "no".')
        answer = input().lower()

    if answer[0] == 'n':
        break