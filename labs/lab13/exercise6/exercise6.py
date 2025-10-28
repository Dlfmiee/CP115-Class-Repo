age = int(input())

# TODO: Your code here
tickets_sold = 0
total_revenue = 0

while True:
    if age == -1:
        break
    elif 0 <= age <= 12:
        total_revenue += 8
        tickets_sold += 1
    elif 13 <= age <= 17:
        total_revenue += 10
        tickets_sold += 1
    elif 18 <= age <= 64:
        total_revenue += 15
        tickets_sold += 1
    elif age >= 65:
        total_revenue += 10
        tickets_sold += 1

    age = int(input())

print(tickets_sold)
print(total_revenue)
