monthly_income = int(input())
credit_score = int(input())
loan_amount = int(input())

# Your code here
approval = 0
if monthly_income >= 4000:
    approval += 1

if credit_score >= 700 :
    interest_rate = 3.5
    approval +=1
elif credit_score >= 600 and credit_score <=699:
    interest_rate = 5.5
    approval +=1
else:
    interest_rate = 0

max_loan_amount = 5*monthly_income
if loan_amount <= max_loan_amount:
    approval +=1

if approval == 3:
    approval_status = "Approved"
else :
    approval_status = "Rejected"

    

print(interest_rate)
print(max_loan_amount)
print(approval_status)