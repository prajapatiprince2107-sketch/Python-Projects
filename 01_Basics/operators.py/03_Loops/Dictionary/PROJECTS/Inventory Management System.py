inventory = {
    "Laptop": {
        "price": 55000,
        "stock": 5
    },
    "Mobile": {
        "price": 25000,
        "stock": 12
    },
    "Keyboard": {
        "price": 2000,
        "stock": 3
    },
    "Monitor": {
        "price": 15000,
        "stock": 8
    },
    "Mouse": {
        "price": 800,
        "stock": 2
    }
}

total_items = 0
total_value = 0
low_stock = 0

for product, details in inventory.items():

    price = details["price"]
    stock = details["stock"]

    value = price * stock

    total_items = total_items + stock
    total_value = total_value + value

    if stock <= 2:
        status = "Critical Stock"
        low_stock = low_stock + 1
    elif stock <= 5:
        status = "Low Stock"
        low_stock = low_stock + 1
    else:
        status = "Available"

    print("Product:", product)
    print("Price:", price)
    print("Stock:", stock)
    print("Stock Value:", value)
    print("Status:", status)
    print("-------------------------")

print("\n========== INVENTORY REPORT ==========")
print("Total Products:", len(inventory))
print("Total Items:", total_items)
print("Total Inventory Value:", total_value)
print("Low Stock Products:", low_stock)