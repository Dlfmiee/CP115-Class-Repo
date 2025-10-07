monthly_income = int(input())
credit_score = int(input())
loan_amount = int(input())

# TODO: Your code here
max_loan_amount = 5 * monthly_income

if monthly_income >= 4000 and credit_score >= 600 and loan_amount <= max_loan_amount:
    if credit_score >= 700:
        interest_rate = 3.5
    else:  # 600–699
        interest_rate = 5.5
    approval_status = "Approved"
else:
    interest_rate = 0.0
    approval_status = "Rejected"

print(interest_rate)
print(max_loan_amount)
print(approval_status)
