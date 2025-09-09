student_gpa = float(input())
total_score = int(input())
number_extracurricular = int(input())
completed_interview = input()

# TODO: Your code here
if student_gpa >= 3.0:
    if total_score >= 1200:
        if number_extracurricular >= 1:
            if completed_interview == "Yes":
                admission_status = "Accepted"
            else:
                admission_status = "Waitlisted"
        else:
            if completed_interview == "Yes":
                admission_status = "Waitlisted"
            else:
                admission_status = "Rejected"
    else:
        if number_extracurricular >= 1:
            if completed_interview == "Yes":
                admission_status = "Waitlisted"
            else:
                admission_status = "Rejected"
        else:
            admission_status = "Rejected"
else:
    if total_score >= 1200:
        if number_extracurricular >= 1:
            if completed_interview == "Yes":
                admission_status = "Waitlisted"
            else:
                admission_status = "Rejected"
        else:
            admission_status = "Rejected"
    else:
        admission_status = "Rejected"



print(admission_status)