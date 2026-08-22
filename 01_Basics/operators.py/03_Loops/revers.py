revers = int(input("Enter ur number: "))
reverse = 0

while revers > 0:
    digit = revers % 10
    reverse = reverse * 10 + digit
    revers = revers // 10

print(reverse)