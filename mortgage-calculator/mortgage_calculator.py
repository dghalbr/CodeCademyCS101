def get_user_input():
    principal = float(input("Enter the loan principal amount: "))
    annual_interest_rate = float(input("Enter the annual interest rate (as a percentage): "))
    years = int(input("Enter the number of years for the loan: "))
    return principal, annual_interest_rate, years

def calculate_monthly_payment(principal, annual_interest_rate, years):
    monthly_interest_rate = annual_interest_rate / 100 / 12
    number_of_payments = years * 12
    monthly_payment = principal * (monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments) / ((1 + monthly_interest_rate) ** number_of_payments - 1)
    return monthly_payment

principal, annual_interest_rate, years = get_user_input()
print(f"Principal: {principal}, Annual Interest Rate: {annual_interest_rate}, Years: {years}")
print(f"Monthly payment: ${calculate_monthly_payment(principal, annual_interest_rate, years):.2f}")