

#age = input("What is your current age?")
#age_as_int = int(age)

#years_remaining = 90 - age_as_int
#days_remaining = years_remaining * 365
#weeks_remaining = years_remaining * 52
#months_remaining = years_remaining * 12


#message = f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left"

#print(message)

print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $\n"))
tip = int(input("How much tip would you like to give? 10, 12 or 15 "))
people = int(input("How many people to split th bill?"))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay ${final_amount}")
