# import
import my_data
import random
import math

print(f"Student: {my_data.student_name}")
print(f"Student ID: {my_data.student_id}")
print(f"Age: {my_data.student_age}")
print(f"Course: {my_data.course_code} - {my_data.course_name}")

random_number = random.randint(70, 95)
print(f"Random Score 1 : {random_number}")
random_number2 = random.randint(75, 100)
print(f"Random score 2 : {random_number2}")

Total = random_number + random_number2
print(f"Total Score: {Total}")

print(f"Name in UpperCase: {my_data.name_upper}")
print(f"Name in LowerCase: {my_data.name_lower}")
print(f"Name length: {my_data.name_length} characters")

square_root = math.sqrt(Total)
print(f"Square root of total score: {square_root}")