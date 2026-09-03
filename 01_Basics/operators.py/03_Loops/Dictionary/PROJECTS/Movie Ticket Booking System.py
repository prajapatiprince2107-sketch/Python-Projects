movies = {
    "Avengers": {
        "price": 250,
        "tickets": 3,
        "rating": 8.7
    },
    "Avatar": {
        "price": 300,
        "tickets": 2,
        "rating": 9.1
    },
    "Batman": {
        "price": 200,
        "tickets": 5,
        "rating": 8.2
    },
    "Interstellar": {
        "price": 350,
        "tickets": 4,
        "rating": 9.3
    }
}

total_tickets = 0
total_revenue = 0
highest_revenue = 0
best_movie = ""

for movie, details in movies.items():

    price = details["price"]
    tickets = details["tickets"]
    rating = details["rating"]

    revenue = price * tickets

    total_tickets = total_tickets + tickets
    total_revenue = total_revenue + revenue

    if revenue > highest_revenue:
        highest_revenue = revenue
        best_movie = movie

    if rating >= 9:
        category = "Excellent"
    elif rating >= 8.5:
        category = "Very Good"
    else:
        category = "Good"

    print("Movie:", movie)
    print("Ticket Price:", price)
    print("Tickets Sold:", tickets)
    print("Rating:", rating)
    print("Revenue:", revenue)
    print("Category:", category)
    print("-------------------------")

print("\n========== MOVIE REPORT ==========")
print("Total Tickets Sold:", total_tickets)
print("Total Revenue:", total_revenue)
print("Highest Revenue:", highest_revenue)
print("Highest Revenue Movie:", best_movie)
print("Average Ticket Price:", total_revenue / total_tickets)