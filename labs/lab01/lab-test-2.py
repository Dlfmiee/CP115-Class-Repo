import random

print("🎯 Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100...")

# Process
number = random.randint(1, 100)
attempts = 0

while True:
    guess = input("Take a guess: ")
    
    if not guess.isdigit():
        print("❌ Please enter a number!")
        continue
    
    guess = int(guess)
    attempts += 1

# Output if guess false

    if guess < number:
        print("📉 Too low! Try again.")
    elif guess > number:
        print("📈 Too high! Try again.")

# Output if guess true
    else:
        print(f"🎉 Correct! The number was {number}.")
        print(f"✅ You guessed it in {attempts} attempts.")
        break

    """HEHEHE BOLEH LA"""
'''yaa'''