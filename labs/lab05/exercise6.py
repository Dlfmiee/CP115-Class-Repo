# INPUT
Times = int(input("Enter Time in minutes: "))

# PROCESS
Remaining_minutes = Times%60
Hours = Times//60

# OUTPUT
print("Minutes : " + str(Times))
print("Hours: " + str(Hours))
print("Remaining minutes: " + str(Remaining_minutes))

