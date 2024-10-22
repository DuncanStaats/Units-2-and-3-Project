'''
Name: Duncan Staats
Date: 10/22/24
Assignment: Unit 2 and 3 Project
'''
while True: 
    month1 = input("Enter the name of the month: ")
    month = month1.title()
    date = int(input("Enter the day (1-31): "))

    if month == "March" and 20 <= date <31 or month == "April" and 1 <= date <= 30 or month == "May" and 1 <= date <= 31 or month == "June" and 1 <= date <= 20:
        print(f"{month} {date} is in Spring.")
        break
    elif month == "June" and 21<= date <= 30 or month == "July" and 1 <= date <= 31 or month == "August" and 1 <= date <= 31 or month == "September" and 1 <= date <= 21:
        print(f"{month} {date} is in Summer")
        break
    elif month == "September" and 22 <= date <= 30 or month == "October" and 1 <= date <= 31 or month == "November" and 1 <= date <= 30 or month == "December" and 1 <= date <= 20:
        print(f"{month} {date} is in Fall")
        break
    elif month == "December" and 21 <= date <= 31 or month == "January" and 1 <= date <= 31 or month == "Febuary" and 1 <= date <= 28 or month == "March" and 1 <= date <= 19:
        print(f"{month} {date} is in Winter")
        break
    print("You have entered an invalid date. Please enter in a correct date.")
    continue
        