position = input()
overtime_hours = int(input())
is_weekend = input()

rate = 1.5
weekend_bonus = 6

if position == "Manager":
    hourly_rate = 35
elif position == "Supervisor":
    hourly_rate = 25
elif position == "Staff":
    hourly_rate = 18
else:
    hourly_rate = 0

overtime_pay = overtime_hours * hourly_rate * rate

if is_weekend.lower() == "yes":
    overtime_pay += overtime_hours * weekend_bonus

total_pay = overtime_pay

print(hourly_rate)
print(overtime_pay)
print(total_pay)