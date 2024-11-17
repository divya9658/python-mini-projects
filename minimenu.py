menu = {
    'Pizza': 80,
    'Pasta': 120,
    'Burger': 90,
    'French Fries': 120,
    'Momos': 50,
    'Coffee': 40,
    'Dessert' : 100,
}
print("Welcome to PYTHON Restaurant, Here is the menu")
print("Pizza: 80\nPasta: 120\nBurger: 90\nFrench Fries: 120\nMomos: 50\nCoffee: 40\nDessert: 100 ")
order_total = 0;
item_1 = input("Enter the name of the item you want to order: ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your order {item_1} is added ")
else:
    print("Sorry, we don't have that item avaiable right now ")
while(True):
    another = input("Do you want to order any other item? (Yes/No)")
    if another == "Yes":
        item_2 = input("Enter the name of the item you want to add to your order: ")
        if item_2 in menu:
            order_total += menu[item_2]
            print(f"Your item {item_2} has been added successfully")
        else:
            print("Sorry, the item you ordered is not avaiable right now")
    else:
        break;

print(f"The bill for your order is {order_total}")
print("Thank you for visiting our restaurant")
