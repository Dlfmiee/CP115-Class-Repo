position = input()
overtime_hours = int(input())
is_weekend = input()

# TODO: Your code here
Position_Hourly = {"Manager": 30, "Supervisor": 20, "Staff": 11, "Intern": 8}
overtime_pay = 0

if position in Position_Hourly:
    base_rate = Position_Hourly[position]

    if overtime_hours <= 8:
        overtime_pay = base_rate * 1.5 * overtime_hours
    else:
        overtime_pay = base_rate * 2 * overtime_hours

    if is_weekend == "Yes":
        overtime_pay += overtime_hours * 5

print(overtime_pay)
