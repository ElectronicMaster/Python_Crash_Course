while True:
    print("-- PRESS Q (or) q TO QUITE")
    first_number = input("Enter First Number: ")
    if(first_number == 'q' or first_number == "Q"):
        break
    second_number = input("Enter Second Number: ")
    if(second_number == 'q' or second_number == "Q"):
        break
    result = 0
    try:
        result = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("Sorry can't divide by 0!")
    else:
        print(f"Result: {result}")