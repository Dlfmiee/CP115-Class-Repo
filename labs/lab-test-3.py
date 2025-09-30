# Programmer Name : MOHAMAD AIDIL FAHMI BIN SAHIMAT
# Problem description : create a Python program that asks the user to enter the monthly usage and then calculates and displays the amount of the bill to be paid after receiving the discount

# INPUT
monthly_usage = float(input("Enter Monthly Usage : "))

# PROCESS
if monthly_usage < 50:
    discount = 0
    print ("No Discount Given")
elif monthly_usage <= 100 :
    discount = 0.05
    print ("Discount : 5%")
elif monthly_usage > 100:
    discount = 0.2
    print ("Discount : 20%")

Discount_Bill = monthly_usage - (monthly_usage*discount)

# OUTPUT
print(f"Bill to be paid : RM{Discount_Bill}")