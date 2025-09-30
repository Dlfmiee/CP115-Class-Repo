num_rounds = int(input())

# TODO: Your code here
# Use input() inside the loop to get each round's score
total_score = 0.0
rounds_processed = 0

for i in range(num_rounds):
    round_score = float(input())
    if round_score > 100:
        round_score = round_score * 1.2   # add 20% bonus
    total_score += round_score
    rounds_processed += 1

final_score = total_score

print(f"{final_score:.1f}")
print(rounds_processed)