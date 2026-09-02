products = {
    "Laptop": 55000,
    "Mobile": 25000,
    "Headphones": 3000,
    "Keyboard": 2000,
    "Monitor": 15000
}

total_price = 0
total_discount = 0

for product, price in products.items():

    if price >= 50000:
        discount = price * 0.15
    elif price >= 20000:
        discount = price * 0.10
    elif price >= 5000:
        discount = price * 0.05
    else:
        discount = 0

    final_price = price - discount

    total_price = total_price + price
    total_discount = total_discount + discount

    print("Product:", product)
    print("Original Price:", price)
    print("Discount:", discount)
    print("Final Price:", final_price)
    print("----------------------")

print("Total Original Price:", total_price)
print("Total Discount:", total_discount)
print("Final Total:", total_price - total_discount)