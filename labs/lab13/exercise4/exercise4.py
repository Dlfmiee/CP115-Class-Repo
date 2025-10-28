number = float(input())

# TODO: Your code here
positive_sum = 0
positive_count = 0

while True:
    if number > 0:
        positive_sum += number
        positive_count += 1
    elif number == 0:
        break
    number = float(input())

print(positive_count)
print(f"{positive_sum:.2f}")
