menu =  {
    "Pizza" : 200,
    "Burger" : 150,
    "Donuts" : 100,
    "Coffee" : 80,
    "Pastry" : 70,
    "Tea" : 50,
}

print("Welcome to FAMILY RESTAURANT")
print("Pizza : Rs200\nBurger : Rs150\nDonuts : Rs100\nCoffee : Rs80\nPastry : Rs70\nTea : Rs50")

order_total = 0

item_1 = input("Enter the name of item which you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} is added to your order")
else:
    print(f"Your item {item_1} is not available yet!")

another_order = input("Do you want to order another item ? (YES/NO) ")
if another_order == "YES":
    item_2 = input("Enter the name of second item  = ")
if item_2 in menu:
    order_total += menu[item_2]
    print(f"Your item {item_2} has been added to your order")
else:
    print(f"Your item {item_2} is not available yet!")
    
print(f"Your bill which you have  to pay is {order_total}")


