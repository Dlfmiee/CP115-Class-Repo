salesman = 0
total_bonus = 0
while salesman <= 5:
    total_sales = input("Enter total sales")
    bonus = 1.2*total_sales
    total_bonus += bonus
    salesman += 1
print(total_bonus)
