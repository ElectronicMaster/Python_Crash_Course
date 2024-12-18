user_0 = {
    "username":"Electro",
    "first":"Saianuush",
    "last":".M.A"
}

for key,value in user_0.items():
    print(f"key: {key}")
    print(f"value: {value}\n")

for key in sorted(user_0.keys()):
    print(key)
print()

for val in set(user_0.values()):
    print(val) 