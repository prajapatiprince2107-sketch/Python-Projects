print("=" * 50)
print("          TAJ HOTEL")
print("=" * 50)

waiter_name = "sanji"
print(f"waiter name : {waiter_name}")
print("welcome to taj hotel")
print("\n1. menu")
print("2. order")
print("3.bill")
print("4.exit")

choice = input("\nenter your choice : ")

if choice == "1":
    print("\n========== menu ==========")
    print("1.veg thali   - 150")
    print("2.non veg thali   - 200")
    print("3.veg biryani   - 120")
    print("4.non veg biryani   - 180")
    
elif choice == "2":
    print("\n========== order ===========")
    print("1.veg thali")
    print("2.non veg thali")
    print("3.veg biryani")
    print("4.non veg biryani")
    
    order = input("select item : ")
    
    if order == "1":
        item = "veg thali"
        price = 150
    elif order == "2":
        item = "non veg thali"
        price = 200
    elif order == "3":
        item = "veg biryani"
        price = 120
    elif order == "4":
        item = "non veg biryani"
        price = 180     
    else:
        print("invalid order")
        exit()          
    print("\n========== bill ==========")
    print(f"waiter name : {waiter_name}")   
    print(f"item : {item}")
    print(f"amount : {price}")
    print("thank you for visiting taj hotel")
elif choice == "4":
    print("thank you! visit again.")    
else:
    print("invalid choice")