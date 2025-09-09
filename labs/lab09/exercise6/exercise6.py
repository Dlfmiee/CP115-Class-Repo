position = input()
overtime_hours = int(input())
is_weekend = input()

# TODO: Your code here
Position_Hourly = {"Manager": 30, "Supervisor": 20, "Staff": 11, "Intern":8}

if position in Position_Hourly and overtime_hours <= 8:
    overtime_pay = Position_Hourly * 1.5
elif position in Position_Hourly and overtime_hours > 8:
    overtime_pay = Position_Hourly * 2

print(overtime_pay)