monthly_income = int(input("Enter monthly income:"))
monthly_expenses = int(input("Enther your total monthly expenses:"))
monthly_savings = monthly_income-monthly_expenses
annual_savings = monthly_savings * 12
interest_on_savings = annual_savings * 0.05
total_savings = annual_savings + interest_on_savings

print("Projected savings for one year, with interest, is: $",total_savings)