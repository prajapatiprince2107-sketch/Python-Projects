numbers = []

n = int(input("How many numbers do you want to enter? "))

for i in range(n):

    number = float(input(f"Enter number {i + 1}: "))
    numbers.append(number)

total = 0
highest = numbers[0]
lowest = numbers[0]

for number in numbers:

    total = total + number

    if number > highest:
        highest = number

    if number < lowest:
        lowest = number

average = total / len(numbers)

print("\n========== NUMBER REPORT ==========")
print("Numbers:", numbers)
print("Total:", total)
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)