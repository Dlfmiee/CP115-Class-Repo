day_type = input()
show_time = int(input())
customer_type = input()
is_student = input()

# TODO your code here
final_price = 0

if show_time > 18:
    final_price += 3

    # Weekday pricing
if day_type == "Weekday" and customer_type == "Adult" and is_student == "Yes":
    base_price = 15.00
    final_price = (final_price + base_price) * 0.9
elif day_type == "Weekday" and customer_type == "Child" and is_student == "Yes":
    base_price = 10.00
    final_price = (final_price + base_price) * 0.9
elif day_type == "Weekday" and customer_type == "Senior" and is_student == "Yes":
    base_price = 12.00
    final_price = (final_price + base_price) * 0.9
elif day_type == "Weekday" and customer_type == "Adult" and is_student == "No":
    base_price = 15.00
    final_price = (final_price + base_price)
elif day_type == "Weekday" and customer_type == "Child" and is_student == "No":
    base_price = 10.00
    final_price = (final_price + base_price)
elif day_type == "Weekday" and customer_type == "Senior" and is_student == "No":
    base_price = 12.00
    final_price = (final_price + base_price)

    # Weekend pricing
elif day_type == "Weekend" and customer_type == "Adult":
    base_price = 18.00
    final_price = (final_price + base_price)
elif day_type == "Weekend" and customer_type == "Child":
    base_price = 12.00
    final_price = (final_price + base_price)
elif day_type == "Weekend" and customer_type == "Senior":
    base_price = 15.00
    final_price = (final_price + base_price)






print(base_price)
print(final_price)