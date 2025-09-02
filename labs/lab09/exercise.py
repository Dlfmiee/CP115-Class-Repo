# Correct: Most specific conditions first
score = 95

if score == 100:
    print("Perfect score!")
elif score >= 90:  
    print("A grade")
elif score >= 80:
    print("B grade")
else:
    print("Below B grade")