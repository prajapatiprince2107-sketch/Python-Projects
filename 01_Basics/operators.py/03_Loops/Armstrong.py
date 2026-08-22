number = int(input("Enter your number: "))
original = number
result = 0
while number > 0:
    digit = number % 10
    cube = digit ** 3
    result = result + cube
    number = number // 10
    if original == result:
        print("Armstrong Number")
    else:
        print("Not Armstrong Number")