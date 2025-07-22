yardLength = float(input())
yardWidth = float(input())
houseLength = float(input())
houseWidth = float(input())
areaOfYard = yardLength * yardWidth
areaOfHouse = houseLength * houseWidth
builtInHouseArea = areaOfYard - areaOfHouse
wage = builtInHouseArea * 2
print(wage)
