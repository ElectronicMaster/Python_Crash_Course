# Cheching whether requested topping in available toppings
available_topping = ["mushroom","olives","green peppers","pepperoni","pineapples","extra cheese"]
requested_topping = ["mushroom","french fries","extra cheese"]

for requested in requested_topping:
    if requested.lower() in available_topping:
        print(f"adding {requested}")
    else:
        print(f"sorry!!! we don't have this {requested}")