products = {
    "Laptop": {
        "price": 55000,
        "quantity": 1
    },
    "Mobile": {
        "price": 25000,
        "quantity": 2
    },
    "Mouse": {
        "price": 800,
        "quantity": 3
    },
    "Keyboard": {
        "price": 2000,
        "quantity": 1
    },
    "Monitor": {
        "price": 15000,
        "quantity": 2
    }
}

subtotal = 0
total_items = 0

for product, details in products.items():

    price = details["price"]
    quantity = details["quantity"]

    item_total = price * quantity

    subtotal = subtotal + item_total
    total_items = total_items + quantity

    print("Product:", product)
    print("Price:", price)
    print("Quantity:", quantity)
    print("Item Total:", item_total)
    print("-------------------------")

if subtotal >= 100000:
    discount = subtotal * 0.15
elif subtotal >= 50000:
    discount = subtotal * 0.10
elif subtotal >= 20000:
    discount = subtotal * 0.05
else:
    discount = 0

after_discount = subtotal - discount

if after_discount >= 50000:
    delivery_charge = 0
else:
    delivery_charge = 500

final_amount = after_discount + delivery_charge

print("\n========== BILL ==========")
print("Total Items:", total_items)
print("Subtotal:", subtotal)
print("Discount:", discount)
print("Delivery Charge:", delivery_charge)
print("Final Amount:", final_amount)