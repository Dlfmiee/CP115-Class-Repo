Price = 120
PriceTraining =  80 
RentLocker = 25
Towel = 15
Registration_Fee = 50

#PROCESS FOR FIRST MONTH
Total_FirstMonth = Price + PriceTraining + RentLocker + Towel + Registration_Fee

#OTHER MONTH
Monthly = Price + PriceTraining + RentLocker + Towel 
Annual_Cost = Total_FirstMonth + (Monthly*11)

print (f"Total First Month : RM{Total_FirstMonth}")
print (f"Monthly Cost After The First Month : RM{Monthly}")
print (f"Annual Cost : RM{Annual_Cost}")