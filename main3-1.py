print("Welcome to Python Pizza Deliveries")
size = input("What size pizza do you want?  S, M or L")
add_peperoni = input("Do you want pepperoni? Y or N")
extra_cheese = input("Do you want extra cheese? Y or N")

bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_peperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
print(f"Your final bill is ${bill}")