import json
import os

def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try: 
        number = float(number_str)
        if number <= 0:
            raise ValueError(messages("prompt_invalid_number"))
    except ValueError:
        return True
    return False

def invalid_interest(percent_str):
    try:
        percent = float(percent_str)
        if percent < 0:
            raise ValueError(messages("prompt_invalid_interest"))
    except ValueError:
        return True
    return False

def messages(message):
    return MESSAGES[message]

with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

def get_loan_amount():
    prompt(messages("prompt_loan_amount"))
    prompt(messages("prompt_loan_amount_example"))
    amount = input()

    while invalid_number(amount):
        prompt(messages("prompt_enter_positive_number"))
        amount = input()

    return int(amount)

def get_interest_rate():
    prompt(messages("prompt_interest_rate"))
    prompt(messages("prompt_interest_rate_example"))
    interest_rate = input() 
    
    while invalid_interest(interest_rate):
        prompt(messages("prompt_enter_positive_number"))
        interest_rate = input()

    return float(interest_rate)

def get_loan_duration():
    prompt(messages("prompt_loan_duration"))
    loan_duration = input()
    
    while invalid_number(loan_duration):
        prompt(messages("prompt_enter_positive_number"))
        loan_duration = input()

    return float(loan_duration)

def calculate_monthly_payment(amount, interest_rate, loan_duration):
    
    interest_rate = (interest_rate / 100) / 12
    loan_duration_months = loan_duration * 12
    
    if interest_rate != 0:
        return round(amount * (interest_rate / 
                               (1 - (1 + interest_rate) ** (-loan_duration_months))),
                               2)
    return round(loan_amount / (loan_duration_months), 2)

def display_result(amount, interest_rate, loan_duration, monthly_payment):
    prompt(messages("prompt_payment_summary").format(amount=amount,
                                                     interest_rate=interest_rate,
                                                     loan_duration=loan_duration,
                                                     monthly_payment=monthly_payment
                                                     ))

def new_calculation():
    prompt(messages("prompt_calculate_another"))
    answer = input().lower()
    while True:
        if answer.startswith('n') or answer.startswith('y'):
            break

        prompt(messages("prompt_calculate_another_answer"))
        answer = input().lower()
    
    return answer

prompt(messages("prompt_welcome_message"))

while True:
    loan_amount = get_loan_amount()
    interest_rate = get_interest_rate()
    loan_duration = get_loan_duration()
    monthly_payment = calculate_monthly_payment(loan_amount, interest_rate, loan_duration)
    display_result(loan_amount, interest_rate, loan_duration, monthly_payment)

    answer = new_calculation()
    if answer == 'y':
        os.system('clear')
    else: 
        break
