import random

randomInteger = random.randint(1, 10)
print(randomInteger)

randomFloat = random.random() * 5
print(randomFloat)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")


states_of_america = ['Alabama',
 'Alaska',
 'Arizona',
 'Arkansas',
 'California',
 'Colorado',
 'Connecticut',
 'Delaware',
 'Florida',
 'Georgia',
 'Hawaii',
 'Idaho',
 'Illinois',
 'Indiana',
 'Iowa',
 'Kansas',
 'Kentucky',
 'Louisiana',
 'Maine',
 'Maryland',
 'Massachusetts',
 'Michigan',
 'Minnesota',
 'Mississippi',
 'Missouri',
 'Montana',
 'Nebraska',
 'Nevada',
 'New Hampshire',
 'New Jersey',
 'New Mexico',
 'New York',
 'North Carolina',
 'North Dakota',
 'Ohio',
 'Oklahoma',
 'Oregon',
 'Pennsylvania',
 'Rhode Island',
 'South Carolina',
 'South Dakota',
 'Tennessee',
 'Texas',
 'Utah',
 'Vermont',
 'Virginia',
 'Washington',
 'West Virginia',
 'Wisconsin',
 'Wyoming']

#states_of_america.extend(['new 1 ', 'new 2'])
#print(states_of_america[3])
#print(states_of_america[-3])
#print(states_of_america)

#names_string = input("Give me everybody's names, separated by a comma. ")
#names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#Get the total number of items in list
#person_who_will_pay = random.choice(names)
#print(person_who_will_pay +  " is goint to buy the meal today!!")

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ['Spinach', 'Potatoes']

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
fruits[-1] = "Melons"
fruits.append("Lemons")
print(fruits)



fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen[1][1])


for vegetable in vegetables:
  print(vegetable)