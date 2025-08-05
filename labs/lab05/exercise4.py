# INPUT
Item_name = input("Enter Item Name: ")
Quantity = int(input("Enter Quantity: "))
Price = float(input("Price Item: "))

# PROCESS
Subtotal = Quantity * Price
Tax = Subtotal * 0.06
Total_Price = Subtotal + Tax

# OUTPUT
print("Subtotal : " + str(Subtotal))
print("Tax : " + str(Tax))
print("Total Price : " + str(Total_Price))
