from datetime import datetime

print("Please enter your date of birth in numerical form when prompted.")
userMonth = int(input("Month: "))
userDate = int(input("Date: "))
userYear = int(input("Year: "))

total_age = (datetime.now() - datetime(userYear, userMonth, userDate))
age_in_seconds = (total_age.days*24*60*60) + total_age.seconds
print("You are", age_in_seconds, "seconds old.")
