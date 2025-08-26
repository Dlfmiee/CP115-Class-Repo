yardLength = float(input("Sila masukkan lenght"))
yardWidth = float(input("Sila masukkan width"))
houseLength = float(input("Sila masukkan houseLength"))
houseWidth = float(input("Sila masukkan housewidth"))
areaOfYard = yardLength * yardWidth
areaOfHouse = houseLength * houseWidth
builtInHouseArea = areaOfYard - areaOfHouse
wage = builtInHouseArea * 2
print(wage)
