target_points = int(input())

# TODO: Your code here
# Use input() inside the while loop to get points each round
total_points = 0
rounds_played = 0

while total_points < target_points:
    points = int(input())
    total_points += points
    rounds_played += 1

rounds_played
print(total_points)
print(rounds_played)