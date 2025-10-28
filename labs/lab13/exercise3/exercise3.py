grade = float(input())

# TODO: Your code here
total_grade = 0
valid_count = 0

while grade != -1:  # stop when -1 is entered
    if 0 <= grade <= 100:      # valid grade
        total_grade += grade
        valid_count += 1

    grade = float(input())

if valid_count > 0:
    average = total_grade / valid_count
else:
    average = 0.00

print(valid_count)
print(f"{average:.2f}")
