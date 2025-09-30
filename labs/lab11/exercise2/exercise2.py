num_days = int(input())
danger_threshold = float(input())

# TODO: Your code here
# Use input() inside the loop to get each day's temperature
danger_days = 0
total_temp = 0

for i in range(1,num_days+1):
    temp = float(input())
    total_temp += temp

    if temp > danger_threshold:
        danger_days += 1

average_temp = total_temp / num_days

print(danger_days)
print(f"{average_temp:.1f}")