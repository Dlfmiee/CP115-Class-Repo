import sys

def main():
    try:
        # Read input from the test framework
        values = list(map(float, sys.stdin.read().split()))
        if len(values) != 4:
            return []

        yardLength, yardWidth, houseLength, houseWidth = values
        areaOfYard = yardLength * yardWidth
        areaOfHouse = houseLength * houseWidth
        builtInHouseArea = areaOfYard - areaOfHouse
        wage = builtInHouseArea * 2

        return [wage]
    except:
        return []

if __name__ == "__main__":
    result = main()
    print(result)
