employee_name = input("Enter Your Name : ")
base_salary = float(input("Base Salary : "))
overtime_hours = int(input("Overtime Hours : "))
tax_status = input("Status : ")

# TODO your code here
if tax_status == "Single":
    if base_salary >= 5000 :
        tax_rate = 0.22
    else tax_rate = 0.18 :
elif tax_status == "Married" :


print(employee_name)
print(tax_rate)
print(f"{net_salary:.2f}")