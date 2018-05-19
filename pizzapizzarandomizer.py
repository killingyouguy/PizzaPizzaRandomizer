# PizzaPizzaRandomizer.py
# Helps you decide what to order at Pizza Pizza

import random

sauce = ["Honey Garlic Sriracha",
         "Buffalo Blue Cheese",
         "Chipotle",
         "No Sauce",
         "Texas Bbq",
         "Creamy Garlic Sauce",
         "Home Style Italian Tomato Sauce",
         "Hot Sauce",
         "Pesto",
         "Pesto and Creamy Garlic",
         "Sweet Chili Thai",
         "Tandoori"]
cheese = ["No Cheese",
          "Mozzarella Cheese",
          "Four Cheese Base",
          "Dairy-free Cheeze"]
toppings = ["Kalamata Olives",
            "Broccoli",
            "Caramelized Onions",
            "Fresh Mushrooms",
            "Green Onions",
            "Green Peppers",
            "Roasted Garlic",
            "Hot Banana Peppers",
            "Jalapeno Peppers",
            "Red Onions",
            "Pineapple",
            "Fire Roasted Red Peppers",
            "Spinach",
            "Roma Tomatoes",
            "Sun-dried Tomatoes",
            "Grilled Zucchini",
            "Bruschetta",
            "Cilantro",
            "Sriracha Chicken",
            "Buffalo Chicken",
            "Chipotle Chicken",
            "Chipotle Steak",
            "Anchovies",
            "Bacon Crumble",
            "Bacon Strips",
            "Grilled Chicken",
            "Capicollo",
            "Chorizo Sausage",
            "Ground Beef",
            "Italian Ham",
            "Spicy Italian Sausage",
            "Steak Strips",
            "Bbq Steak Strips",
            "New York Style Pepperoni",
            "Pepperoni",
            "Pesto Chicken",
            "Salami",
            "Meatballs",
            "Feta Cheese",
            "Parmesan Cheese",
            "Extra Cheese",
            "Four Cheese Blend Topping",
            "Goat Cheese",
            "Extra Dairy-Free Cheeze",
            "Balsamic Vinegar",
            "Chili Peppers",
            "Italiano Blend Seasoning",
            "Olive Oil",
            "Sweet Garlic and Pepper Seasoning",
            "Tabasco Sauce",
            "Texas Bbq Sauce on Top"]

def getRandom(arr):
    return arr[random.randint(0, len(arr)-1)]

print("""PIZZA PIZZA RANDOMIZER
by Killingyouguy

We're preparing your special pizza...""")

print("Your base sauce is: {0}".format(getRandom(sauce)))
print("Your base cheese is: {0}".format(getRandom(cheese)))

for side in ["Left", "Right"]:
    for i in range(0, 3):
        print("{0} side's special topping #{1} is: {2} ({3}X)".format(side,
                                                                      i+1,
                                                                      getRandom(toppings),
                                                                      random.randint(1, 4)))

print("\nEnjoy!!")
input("Press enter to exit...")



