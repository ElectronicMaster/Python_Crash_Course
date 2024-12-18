unconfirmed_user = ["Saianuush","Hima","Jishnu","Thiru","Gokul","Guruprasad","Santhos","Srivatsa"]
confirmed_user = []

while unconfirmed_user:
    user = unconfirmed_user.pop()
    print(f"Confirmed user : {user}")
    confirmed_user.append(user)
print(unconfirmed_user)
print(confirmed_user)