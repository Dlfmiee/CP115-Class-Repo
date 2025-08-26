import employee_data

# employee_data.basic_salary, employee_data.overtime_hours, and employee_data.overtime_rate

Medical_Insurance = 50
Parking = 30

#DEDUCTION
DeductionSOCSO = employee_data.basic_salary * 0.5
DeductionEIS = employee_data.basic_salary * 0.2
DeductionEPF = employee_data.basic_salary * 0.11
TotalDeduction = DeductionEIS + DeductionEPF + DeductionSOCSO

#PROCESS
Overtime = employee_data.overtime_hours * employee_data.overtime_rate
Payslip = employee_data.basic_salary + Overtime
Total_Salary = (employee_data.basic_salary - TotalDeduction) - Medical_Insurance - Parking + Overtime

#OUTPUT
print(f"Payslip : RM{Payslip}")
print(f"Deduction Amount From EPF : RM{DeductionEPF}")
print(f"Deduction Amount From SOCSO : RM{DeductionSOCSO}")
print(f"Deduction Amount From EIS : RM{DeductionEIS}")
print(f"Total Deduction : RM{TotalDeduction}")
print(f"Net Salary : RM{TotalDeduction}")