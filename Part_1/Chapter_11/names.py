from name_function import get_formatted_name

print("Press 'q' any time to quit.")
while True:
    first = input("Enter First name : ")
    if first == 'q':
        break
    last = input("Enter Last name : ")
    if last == 'q':
        break
    formatted_name = get_formatted_name(first,last)
    print(f"Neatly formatted name : {formatted_name}")   