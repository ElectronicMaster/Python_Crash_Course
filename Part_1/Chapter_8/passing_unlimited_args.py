def pizza(bread,*toppings):
    print(list(toppings))
    toppings = list(toppings)
    toppings[1] = "tomato"
    print(f"Pizza Base: {bread}")
    print("Requested toppings are:")
    for topping in toppings:
        print(topping)

pizza("Hand Tossed", "paneer", "Mashroom", "Extra Cheese")

