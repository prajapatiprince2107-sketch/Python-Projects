numbers = [[1, 2], [3, 4], [5, 6]]

result = [num for row in numbers for num in row if num % 2 == 0]

print(result)