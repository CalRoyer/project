'''
Cal Royer
1/24/25
Unit 2 and 3 Project
'''

month = input("Enter the name of a month: ")
day = int(input("Enter the day (1-31): "))

def season(month, day):
    if (month == "March" and day >= 20) or month == "April" or month == "May" or (month == "June" and day <= 20):
        return "Spring"
    elif (month == "June" and day >= 21) or month == "July" or month == "August" or (month == "September" and day <= 21):
        return "Summer"
    elif (month == "September" and day >= 22) or month == "October" or month == "November" or (month == "December" and day <= 20):
        return "Fall"
    else:
        return "Winter"
    
print(f"{month} {day} is in {season(month, day)}")
