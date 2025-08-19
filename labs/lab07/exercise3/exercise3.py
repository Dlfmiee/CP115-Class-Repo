# import
import school_data
import random
import math

print(f"Student: {school_data.student_name}")
print(f"Student ID: {school_data.student_id}")
print(f"Age: {school_data.student_age}")
print(f"Course: {school_data.course_code} - {school_data.course_name}")

random_number = random.randint(70, 95)
print(f"Random Score 1 : {random_number}")
random_number2 = random.randint(75, 100)
print(f"Random score 2 : {random_number2}")

Total = random_number + random_number2
print(f"Total Score: {Total}")

print(f"Name in UpperCase: {school_data.name_upper}")
print(f"Name in LowerCase: {school_data.name_lower}")
print(f"Name length: {school_data.name_length} characters")

square_root = math.sqrt(Total)
print(f"Square root of total score: {square_root}")