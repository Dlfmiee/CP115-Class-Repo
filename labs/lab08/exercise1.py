score1 = 85
score2 = 92.5
score3 = 78

average = (score1 + score2 + score3)/3

print (f"Average : {average} (Type : {type(average)}) ")
print (f"Average : {average} (Type : {type(int(average))}) ")

x = score1 ** 2 / score2 + score3 % 7
print (f"score1 ** 2 / score2 + score3 % 7 : {x} (Type : {type(x)}) ")

#Compare what happens with: int(score2) vs float(score1), why the results is like that?
#Class type is float because score 1 is float

