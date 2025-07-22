principal = float(input())
rate = float(input())
time = float(input())
interest = principal * rate * time
totalAmount = principal * 1 + rate / 100
monthlyInterest = principal + principal * rate * time * 12 / 100 * 12
print(interest)
print(totalAmount)
print(monthlyInterest)
