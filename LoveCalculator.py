print("Welcome to the Love Calculator.")
name1 = input("What is your name? --> ")
name2 = input("What is their name? --> ")
combined_String = name1.lower() + name2.lower()
t = combined_String.count('t')
r = combined_String.count('r')
u = combined_String.count('u')
e = combined_String.count('e')
true = t+r+u+e
l = combined_String.count('l')
o = combined_String.count('o')
v = combined_String.count('v')
e = combined_String.count('e')
love = l+o+v+e
score = int(str(true) + str(love))
if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score>40 and score<50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")
