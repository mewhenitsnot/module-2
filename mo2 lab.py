#Jonathan lewis
#MO3 Lab
student_last_name = input("enter your last name")
if student_last_name == "zzz":
    exit(0)
student_first_name = input("enter your first name")
GPA = float(input("enter your GPA"))
if GPA >= 3.5:
    print("you have made the deans list!")
elif GPA >= 3.25:
    print("you have made the honor roll!")