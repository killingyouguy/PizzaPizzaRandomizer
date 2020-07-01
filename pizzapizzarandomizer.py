# PizzaPizzaRandomizer.py
# Helps you decide what to order at Pizza Pizza

import random

size = ["Small",
        "Medium",
        "Large",
        "Extra Large"]
dough = ["Regular",
         "Whole Grain"]
thiccness = ["Regular", 
             "Thin", 
             "Thick"]
sauce = ["Buffalo Blue Cheese",
         "Chipotle",
         "No Sauce",
         "Texas Bbq",
         "Creamy Garlic Sauce",
         "Home Style Italian Tomato Sauce",
         "Hot Sauce",
         "Pesto",
         "Sweet Chili Thai",
         "Tandoori"]
cheese = ["No Cheese",
          "Mozzarella Cheese",
          "Four Cheese Base",
          "Dairy-free Cheeze"]
toppings = [# Veg
            "Artichokes",
            "Broccoli",
            "Bruschetta",
            "Cilantro",
            "Caramelized Onions",
            "Fire Roasted Red Peppers",
            "Fresh Mushrooms",
            "Green Onions",
            "Green Peppers",
            "Grilled Zucchini",
            "Hot Banana Peppers",
            "Jalapeno Peppers",
            "Kalamata Olives",
            "Pineapple",
            "Plant-based Chorizo Crumble",
            "Plant-based Pepperoni",
            "Red Onions",
            "Roasted Garlic",
            "Roma Tomatoes",
            "Spinach",
            "Sun-dried Tomatoes",
            # Meat
            "Anchovies",
            "Bacon Crumble",
            "Bacon Strips",
            "Buffalo Chicken",
            "Chipotle Chicken",
            "Chipotle Steak",
            "Chorizo Sausage",
            "Grilled Chicken",
            "Ground Beef",
            "Italian Ham",
            "New York Style Pepperoni",
            "Pepperoni",
            "Salami",
            "Spicy Italian Sausage",
            "Steak Strips",
            # Cheese
            "Extra Cheese",
            "Extra Dairy-Free Cheeze",
            "Feta Cheese",
            "Four Cheese Blend Topping",
            "Goat Cheese",
            "Parmesan Cheese",
            # Free
            "Chili Peppers",
            "Italiano Blend Seasoning",
            "Olive Oil",
            "Sweet Garlic and Pepper Seasoning",
            "Tabasco Sauce",
            "Texas Bbq Sauce on Top"]

def getRandom(arr):
    return arr[random.randint(0, len(arr)-1)]
    
def flipCoin():
    return bool(random.getrandbits(1))

print("""PIZZA PIZZA RANDOMIZER
by Killingyouguy

We're preparing your special pizza...\n""")

print("You're getting a {0} pizza!".format(getRandom(size)))
print("Your dough is {0} {1} crust".format(getRandom(dough), 
                                                  getRandom(thiccness)))
print("Your base sauce is: {0}".format(getRandom(sauce)))
print("Your base cheese is: {0}".format(getRandom(cheese)))

sides = ["Left side", "Right side", "Centre"]

for side in sides:
    for i in range(0, random.randint(0, 3)):
        print("{0}'s special topping #{1} is: {2} ({3}X)".format(side,
                                                                      i+1,
                                                                      getRandom(toppings),
                                                                      random.randint(1, 4)))

print("\nEnjoy!!")
input("Press enter to exit...")



