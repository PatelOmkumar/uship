import datetime

def calculate_year_of_100(age):
    current_year = datetime.datetime.now().year
    years_to_100 = 100 - age
    year_of_100 = current_year + years_to_100
    return year_of_100

name = input("Enter your name: ")
age = int(input("Enter your age: "))

year_of_100 = calculate_year_of_100(age)
message = f"Hi {name}, you will turn 100 years old in the year {year_of_100} when you will be {100} years old."
print(message)
