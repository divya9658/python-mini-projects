print("Welcome to the Tip Calculator.")
bill = float(input("What was the total bill? Rs "))
Tip = int(input("What pecentage tip would you like to give? 10, 12, or 15? "))
Persons = int(input("How many people to split the bill? "))
Total_bill = bill*(1+ Tip/100)
Total = Total_bill/Persons
print(f"Each person should pay: Rs {round(Total,2)}")



