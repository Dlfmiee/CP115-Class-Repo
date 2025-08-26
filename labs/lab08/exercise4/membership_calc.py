# Membership and services cost (RM)
Price = 120              # Base membership per month
PriceTraining = 80       # Cost per personal training session
TrainingSessions = 6     # Number of personal training sessions
RentLocker = 25          # Locker rental per month
Towel = 15               # Towel service per month
Registration_Fee = 50    # One-time registration fee

# PROCESS FOR FIRST MONTH
Total_FirstMonth = (Price + (PriceTraining * TrainingSessions) + RentLocker + Towel + Registration_Fee)

# PROCESS FOR OTHER MONTHS (without registration fee)
Monthly = (Price + (PriceTraining * TrainingSessions) + RentLocker + Towel)

# ANNUAL COST (12 months, first month includes registration fee)
Annual_Cost = Total_FirstMonth + (Monthly * 11)

# OUTPUT
print(f"Total First Month : RM{Total_FirstMonth}")
print(f"Monthly Cost After The First Month : RM{Monthly}")
print(f"Annual Cost : RM{Annual_Cost}")
