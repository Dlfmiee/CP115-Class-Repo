kWh = float(input("Enter Usage : "))
charges = None
if kWh <= 100:
    charges = kWh*0.30
elif kWh <= 200 :
    charges = ((kWh-100)*0.50)+30
else:
    charges = ((kWh-200)*0.75)+50+30

(print(f"Total bill : {charges}"))