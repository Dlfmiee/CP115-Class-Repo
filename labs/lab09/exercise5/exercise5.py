main_course = input()
drink = input()
dessert = input()
customer_age = int(input())

# TODO: Your code here
main_course_prices = {"Chicken": 10, "Beef": 12, "Fish": 11}
drink_prices = {"Soft Drink": 2, "Coffee": 3}
dessert_prices = {"Ice Cream": 4, "Cake": 5}

price = 0
if main_course in main_course_prices:
    price += main_course_prices[main_course]
if drink in drink_prices:
    price += drink_prices[drink]
if dessert in dessert_prices:
    price += dessert_prices[dessert]

service = price * 1.10

final_bill = service
if customer_age > 60:  # Senior citizen
    final_bill *= 0.85
elif customer_age < 18:  # Student
    final_bill *= 0.90


print(f"{final_bill:.2f}")
