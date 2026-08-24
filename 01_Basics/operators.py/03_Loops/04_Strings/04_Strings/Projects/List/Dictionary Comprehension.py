numbers = [10, 15, 20, 25, 30, 35, 40]

num =  {num: num ** 2 for  num in numbers if num % 2 == 0}

print(num)