import random
# INPUT
StudentsClass = input("Enter Students Class: ")

# PROCESS
random_number = random.randint(1, 100)

if StudentsClass == "C01":
    StudentsList = ['Aidil', 'Shah', 'Iskadar', 'Yohannes', 'Chris','Hafiz','Sahirah','Ain','Cheng','Rabbiatul','Wiyah','Lionel','Syafiee']
else:
    StudentsList = ['Abdul', 'Azmin', 'Aiman', 'Wafi', 'Blessley','Fahrin','Batrisya','Ave','Tira','Siti','Syadiq','Dorothy','Allyne','Mia','Wane']

random_choice = random.choice(StudentsList)

# OUTPUTT
print("Random Number: " + str(random_number))
print("Randomly selected student: " + random_choice)
print("Class information: " + StudentsClass)
