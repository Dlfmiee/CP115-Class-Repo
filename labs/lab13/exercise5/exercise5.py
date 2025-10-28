amount = int(input())

# TODO: Your code here
valid_count = 0
total_withdrawn = 0

while True:
    if amount == 0:
        break
    elif amount < 20 or amount > 500 or amount % 20 != 0:
        amount = int(input())
        continue
    else:
        valid_count += 1
        total_withdrawn += amount
        amount = int(input())

print(valid_count)
print(total_withdrawn)
