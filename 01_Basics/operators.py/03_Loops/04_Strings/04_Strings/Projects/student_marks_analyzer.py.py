marks = [78, 65, 90, 55, 82]

for mark in marks:
    if mark >= 40:
        print(mark, "High")
    else:
        print(mark, "Low")
total = sum(marks)
print(total)
average = total / len(marks)
print("Average:", average)
if average >= 40:
    print("Pass")
else:
    print("Fail")