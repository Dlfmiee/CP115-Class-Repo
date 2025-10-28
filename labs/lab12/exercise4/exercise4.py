score_input = input()

# TODO: Your code here
passing_count = 0
failing_count = 0

while score_input != "end":
    score = float(score_input)

    if score >= 60:
        passing_count += 1
    else:
        failing_count += 1
    
    score_input = input()

total_students = passing_count + failing_count
if total_students > 0:
    pass_rate = (passing_count / total_students) * 100
else:
    pass_rate = 0

print(passing_count)
print(failing_count)
print(f"{pass_rate:.2f}")
