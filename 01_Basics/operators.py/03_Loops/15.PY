number = int(input("Enter a positive number: "))

even = 0
odd = 0
total = 0
i = 1

while i <= number:

    if i % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

    total = total + i
    i = i + 1

print("\n===== RESULT =====")
print("Even numbers:", even)
print("Odd numbers:", odd)
print("Total:", total)