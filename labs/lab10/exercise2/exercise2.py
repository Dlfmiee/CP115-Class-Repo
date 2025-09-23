age = int(input())
accident_count = int(input())

# Your code here
penalty = 0
rate = 0
final_premium = 0
if age < 25 :
    base_premium = 2400
elif age >= 25 and age <= 50 :
    base_premium = 1800
elif age > 50:
    base_premium = 2000
if accident_count == 0 :
    penalty = 0
elif accident_count <= 2 and accident_count >= 1:
    penalty = 300
elif accident_count >= 3:
    penalty = 600

if penalty == 0 :
    rate = 0.1

discount_amount = base_premium*rate
final_premium = base_premium - discount_amount + penalty

discount_amount=int(discount_amount)
final_premium=int(final_premium)

print(base_premium)
print(final_premium)
print(discount_amount)