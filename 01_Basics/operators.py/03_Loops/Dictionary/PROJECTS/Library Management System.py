library = {
    "book1": {
        "title": "Python Basics",
        "author": "John",
        "price": 800,
        "available": True
    },
    "book2": {
        "title": "Learn SQL",
        "author": "David",
        "price": 600,
        "available": False
    },
    "book3": {
        "title": "Advanced Python",
        "author": "Alex",
        "price": 1200,
        "available": True
    },
    "book4": {
        "title": "Web Development",
        "author": "Robert",
        "price": 900,
        "available": True
    }
}

total_books = 0
available_books = 0
unavailable_books = 0
total_value = 0

for book_id, details in library.items():

    total_books = total_books + 1
    total_value = total_value + details["price"]

    print("Book ID:", book_id)
    print("Title:", details["title"])
    print("Author:", details["author"])
    print("Price:", details["price"])

    if details["available"] == True:
        print("Status: Available")
        available_books = available_books + 1
    else:
        print("Status: Not Available")
        unavailable_books = unavailable_books + 1

    print("-------------------------")

print("\n========== LIBRARY REPORT ==========")
print("Total Books:", total_books)
print("Available Books:", available_books)
print("Unavailable Books:", unavailable_books)
print("Total Book Value:", total_value)
print("Average Book Price:", total_value / total_books)