from functools import reduce

numbers = []

n = int(input("How many numbers? "))

for i in range(n):
    number = int(input(f"Enter number {i + 1}: "))
    numbers.append(number)

print("\nOriginal Numbers:", numbers)

squares = list(map(lambda x: x * x, numbers))

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

total = reduce(lambda a, b: a + b, numbers)

print("Squares:", squares)
print("Even Numbers:", even_numbers)
print("Total:", total)