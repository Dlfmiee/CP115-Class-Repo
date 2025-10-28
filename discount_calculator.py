# CP115 Assignment: Discount Calculator
# Name: MOHAMAD AIDIL FAHMI BIN SAHIMAT
# Matric No: MC2515113641

age = input("Enter your age ( Integer ): ")
ticket_price = input("Enter the ticket price ( Floating-point number ): ")

# Validate numeric input
if not age.isdigit() or not ticket_price.replace('.', '', 1).isdigit():
    print("Error")
else:
    age = int(age)
    ticket_price = float(ticket_price)

    # check negative values
    if age < 0 or ticket_price < 0:
        print("Error")
    else:
        # Determine category and discount
        if age <= 12:
            category = "Children"
            discount = 0.50
        elif age <= 17:
            category = "Teenagers"
            discount = 0.25
        else:
            category = "Adults"
            discount = 0.0

        # Calculate discounted price
        discount_price = ticket_price - (discount * ticket_price)

        # Display output
        print(f"You are eligible for the {category} discount ({discount*100:.0f}% off).")
        print(f"Discounted ticket price: ${discount_price:.2f}")
