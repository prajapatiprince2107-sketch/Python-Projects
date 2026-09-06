numbers = []

n = int(input("How many numbers? "))

for i in range(n):
    number = int(input(f"Enter number {i + 1}: "))
    numbers.append(number)

squares = [x * x for x in numbers]

even_numbers = [x for x in numbers if x % 2 == 0]

odd_numbers = [x for x in numbers if x % 2 != 0]

greater_than_10 = [x for x in numbers if x > 10]

print("\nOriginal:", numbers)
print("Squares:", squares)
print("Even Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)
print("Greater Than 10:", greater_than_10)