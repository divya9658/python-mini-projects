print("Welcome to the Python Pizza Deliveries!")
print("Small Pizza: Rs15/-\nMedium Pizza: Rs20/-\nLarge Pizza: Rs25/-")
print("\nPepperoni for Small Pizza: + Rs2/-\nPepperoni for Medium or Large Pizza: + Rs3/-")
print("\nExtra Cheese for any Pizza: + Rs1")
size = input("What size pizza do you want? S,M,or L -->")
add_pepperoni = input("Do you want pepperoni? Y or N -->")
extra_cheese = input("Do you want extra cheese? Y or N -->")
if size == 'S':
    bill = 15
    if add_pepperoni == 'Y':
       bill = bill + 2
elif size == 'M':
    bill = 20
    if add_pepperoni == 'Y':
       bill = bill + 3
else:
    bill = 25
    if add_pepperoni == 'Y':
       bill = bill + 3

if extra_cheese == 'Y':
    bill = bill + 1

print(f"Your final bill is Rs{bill}")