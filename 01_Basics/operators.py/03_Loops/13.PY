total = 0

while True:

    print("\n===== SHOPPING =====")
    print("1. Add Item")
    print("2. Show Total")
    print("3. Checkout")

    choice = int(input("Enter choice: "))

    if choice == 1:

        item = input("Enter item name: ")
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))

        item_total = price * quantity
        total = total + item_total

        print(item, "added!")
        print("Item total:", item_total)

    elif choice == 2:
        print("Current Total:", total)

    elif choice == 3:
        print("\n===== FINAL BILL =====")
        print("Total Amount:", total)
        print("Thank you for shopping! 🛍️")
        break

    else:
        print("Invalid choice!")