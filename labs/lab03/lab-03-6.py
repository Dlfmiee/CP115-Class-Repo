yardLength = float(input())
yardWidth = float(input())
houseLength = float(input())
houseWidth = float(input())
areaOfYard = yardLength * yardWidth
areaOfHouse = houseLength * houseWidth
builtInHouseArea = areaOfHouse - areaOfYard
wage = builtInHouseArea * 2
print(wage)
