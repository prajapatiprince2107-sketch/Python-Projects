while True:

    print("\n===== CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 5:
            print("Calculator closed! 👋")
            break

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            result = num1 + num2

        elif choice == 2:
            result = num1 - num2

        elif choice == 3:
            result = num1 * num2

        elif choice == 4:
            result = num1 / num2

        else:
            print("Invalid choice!")
            continue

        print("Result:", result)

    except ValueError:
        print("Please enter numbers only! ❌")

    except ZeroDivisionError:
        print("Cannot divide by zero! ❌")