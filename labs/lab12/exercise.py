# Sentinel-controlled approach - stop when ready
total = 0
count = 0

number = int(input("Enter number (0 to stop): "))  # Prime input

while number != 0:  # Condition
    total += number
    count += 1
    number = int(input("Enter number (0 to stop): "))  # Update

print(f"Total of {count} numbers: {total}")