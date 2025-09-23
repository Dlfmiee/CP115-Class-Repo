import math

for i in range(4):
    radius = float(input(f"Enter radius {i+1}: "))
    if radius > 0:
        area = math.pi * radius ** 2
        print(f"Area of circle {i+1}: {area:.2f}")
    else:
        print("Invalid radius, must be positive!")
        break