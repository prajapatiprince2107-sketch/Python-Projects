import re

phone = input("Enter your phone number: ")

pattern = r"^[6-9][0-9]{9}$"

if re.match(pattern, phone):
    print("Valid Indian Mobile Number ✅")
else:
    print("Invalid Mobile Number ❌")