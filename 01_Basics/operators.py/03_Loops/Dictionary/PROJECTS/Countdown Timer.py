import time

seconds = int(input("Enter countdown time in seconds: "))

while seconds > 0:

    minutes = seconds // 60
    remaining_seconds = seconds % 60

    print(
        f"{minutes:02d}:{remaining_seconds:02d}",
        end="\r"
    )

    time.sleep(1)

    seconds = seconds - 1

print("\n⏰ Time's Up!")