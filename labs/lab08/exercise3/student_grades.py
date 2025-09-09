Score1 = 78
Score2 = 85
Score3 = 92
Score4 = 67
Score5 = 88

#Caculate Total and Average
Total_Points = Score1 + Score2 + Score3 + Score4 + Score5
Average = Total_Points/500

#Calculate Percentage each score
Percentage1 = (Score1/Total_Points)*100
Percentage2 = (Score2/Total_Points)*100
Percentage3 = (Score3/Total_Points)*100
Percentage4 = (Score4/Total_Points)*100
Percentage5 = (Score5/Total_Points)*100

#OUTPUT
print(f"Score 1 : {Score1}\nScore 2 : {Score2}\nScore 3 : {Score3}\nScore 4 : {Score4}\nScore 5 : {Score5}\n")
print(f"Total Points : {Total_Points}")
print(f"Average : {Average}")
print(f"Percentage Score 1 : {Percentage1:.0f}%\nPercentage Score 2 : {Percentage2:.0f}%\nPercentage Score 3 : {Percentage3:.0f}%\nPercentage Score 4 : {Percentage4:.0f}%\nPercentage Score 5 : {Percentage5:.0f}%\n")


