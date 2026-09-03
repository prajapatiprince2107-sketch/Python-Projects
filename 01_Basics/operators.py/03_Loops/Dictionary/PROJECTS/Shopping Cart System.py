cart = {}

n = int(input("Enter number of products: "))

for i in range(n):

    product = input("Enter product name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    cart[product] = {
        "price": price,
        "quantity": quantity
    }

subtotal = 0

print("\n========== CART ==========")

for product, details in cart.items():

    price = details["price"]
    quantity = details["quantity"]

    total = price * quantity
    subtotal = subtotal + total

    print("Product:", product)
    print("Price:", price)
    print("Quantity:", quantity)
    print("Total:", total)
    print("-------------------------")

if subtotal >= 5000:
    discount = subtotal * 0.10
elif subtotal >= 2000:
    discount = subtotal * 0.05
else:
    discount = 0

final_amount = subtotal - discount

print("Subtotal:", subtotal)
print("Discount:", discount)
print("Final Amount:", final_amount)