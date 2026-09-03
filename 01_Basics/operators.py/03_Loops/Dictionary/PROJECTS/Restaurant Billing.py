menu = {}

n = int(input("Enter number of items: "))

for i in range(n):

    item = input("Enter item name: ")
    price = float(input("Enter item price: "))
    quantity = int(input("Enter quantity: "))

    menu[item] = {
        "price": price,
        "quantity": quantity
    }

subtotal = 0
total_items = 0

print("\n========== ORDER DETAILS ==========")

for item, details in menu.items():

    price = details["price"]
    quantity = details["quantity"]

    item_total = price * quantity

    subtotal = subtotal + item_total
    total_items = total_items + quantity

    print("Item:", item)
    print("Price:", price)
    print("Quantity:", quantity)
    print("Item Total:", item_total)
    print("-------------------------")

if subtotal >= 1000:
    discount = subtotal * 0.10
elif subtotal >= 500:
    discount = subtotal * 0.05
else:
    discount = 0

tax = (subtotal - discount) * 0.05
final_bill = subtotal - discount + tax

print("\n========== FINAL BILL ==========")
print("Total Items:", total_items)
print("Subtotal:", subtotal)
print("Discount:", discount)
print("Tax:", tax)
print("Final Bill:", final_bill)