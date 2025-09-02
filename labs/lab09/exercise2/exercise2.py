employee_name = input("Enter Your Name : ")
base_salary = float(input("Base Salary : "))
overtime_hours = int(input("Overtime Hours : "))
tax_status = input("Status : ")

# TODO your code here

if tax_status == "Single":
    if base_salary >= 5000 :
        tax_rate = 0.22
    else:
        tax_rate = 0.18
elif tax_status == "Married":
    if base_salary >= 6000:
        tax_rate = 0.20
    else:
        tax_rate = 0.15
else:
    if base_salary >= 5500:
        tax_rate = 0.25
    else:
        tax_rate = 0.19

overtime_pay = 35 * overtime_hours
gross_income = base_salary + overtime_pay
net_salary = gross_income*tax_rate*0.89*0.5

print(employee_name)
print((tax_rate))
print(f"{net_salary:.2f}")
