rooms = {
    101: {
        "guest": "Rahul",
        "room_type": "Single",
        "price": 1500,
        "days": 3
    },
    102: {
        "guest": "Amit",
        "room_type": "Double",
        "price": 2500,
        "days": 2
    },
    103: {
        "guest": "Priya",
        "room_type": "Deluxe",
        "price": 4000,
        "days": 5
    },
    104: {
        "guest": "Neha",
        "room_type": "Single",
        "price": 1500,
        "days": 4
    }
}

total_bill = 0
highest_bill = 0
highest_guest = ""

for room_number, details in rooms.items():

    price = details["price"]
    days = details["days"]

    bill = price * days

    total_bill = total_bill + bill

    if bill > highest_bill:
        highest_bill = bill
        highest_guest = details["guest"]

    if bill >= 15000:
        category = "VIP"
    elif bill >= 5000:
        category = "Premium"
    else:
        category = "Regular"

    print("Room Number:", room_number)
    print("Guest:", details["guest"])
    print("Room Type:", details["room_type"])
    print("Price Per Day:", price)
    print("Days:", days)
    print("Total Bill:", bill)
    print("Category:", category)
    print("-------------------------")

print("\n========== HOTEL REPORT ==========")
print("Total Rooms:", len(rooms))
print("Total Revenue:", total_bill)
print("Average Bill:", total_bill / len(rooms))
print("Highest Bill:", highest_bill)
print("Highest Paying Guest:", highest_guest)