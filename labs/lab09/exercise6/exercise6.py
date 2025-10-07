position = input()
overtime_hours = int(input())
is_weekend = input()

# TODO: Your code here
Position_Hourly = {"Manager": 30, "Supervisor": 20, "Staff": 15, "Intern": 8}
overtime_pay = 0

if position in Position_Hourly:
    base_rate = Position_Hourly[position]

    if overtime_hours <= 8:
        overtime_pay = base_rate * 1.5 * overtime_hours
    else:
        overtime_pay = (8 * base_rate * 1.5) + ((overtime_hours - 8) * base_rate * 2)

    if is_weekend.lower() == "yes":
        overtime_pay += overtime_hours * 5

print(overtime_pay)
