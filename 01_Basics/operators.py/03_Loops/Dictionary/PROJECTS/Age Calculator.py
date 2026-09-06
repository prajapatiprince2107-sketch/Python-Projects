from datetime import date

name = input("Enter your name: ")

birth_year = int(input("Enter your birth year: "))
birth_month = int(input("Enter your birth month: "))
birth_day = int(input("Enter your birth day: "))

today = date.today()

birth_date = date(birth_year, birth_month, birth_day)

age = today.year - birth_date.year

if (today.month, today.day) < (birth_date.month, birth_date.day):
    age = age - 1

print("\n========== AGE DETAILS ==========")
print("Name:", name)
print("Birth Date:", birth_date)
print("Today's Date:", today)
print("Your Age:", age)