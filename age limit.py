from datetime import datetime

dob = input("Enter DOB (DD-MM-YYYY): ")
try:
    d = datetime.strptime(dob, '%d-%m-%Y')
    t = datetime.today()
    age = t.year - d.year - ((t.month,t.day)<(d.month,d.day))
    print("Age:", age)
    if age<18: print("Underage")
    elif age<60: print("Working age")
    else: print("Retirement age")
except:
    print("Invalid date format")
