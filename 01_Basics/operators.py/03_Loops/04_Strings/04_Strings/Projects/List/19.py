numbers = [1, 2, 3, 4, 5]

result = [num * 10 if num % 2 == 0 else num * 5 for num in numbers]

print(result)