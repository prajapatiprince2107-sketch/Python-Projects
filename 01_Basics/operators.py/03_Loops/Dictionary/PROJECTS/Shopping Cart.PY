cart = {
    "Laptop": {
        "price": 55000,
        "quantity": 1
    },
    "Mouse": {
        "price": 1200,
        "quantity": 2
    },
    "Keyboard": {
        "price": 2500,
        "quantity": 1
    },
    "Headphones": {
        "price": 3000,
        "quantity": 2
    }
}

grand_total = 0
total_items = 0

for product, details in cart.items():

    price = details["price"]
    quantity = details["quantity"]

    item_total = price * quantity

    grand_total = grand_total + item_total
    total_items = total_items + quantity

    print("Product:", product)
    print("Price:", price)
    print("Quantity:", quantity)
    print("Item Total:", item_total)
    print("----------------------")

print("Total Items:", total_items)
print("Grand Total:", grand_total)