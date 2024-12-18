def build_profile(first,last,**user_info):
    user_info["first_name"] = first
    user_info["last_name"] = last
    for info in user_info.values():
        print(info)
    return user_info

user_info = build_profile("Sai","Anuush",location="Chennai",Field="CSC")
# user_info = build_profile("Sai","Anuush",location="Chennai",Field="CSC","Hello") // Syntax Error
print(user_info)