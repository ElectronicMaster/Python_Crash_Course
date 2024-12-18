# Changing Case in a String with Methods (temporary)

name = "saianuush"
print(name.title())
print(name.upper())
print(name.lower())
print(name)

# Using Variables in String

FirstName = "saianuush"
LastName = "M.A."
print(f"\nFirst Name : {FirstName} and Last Name : {LastName}")
print(f"First Name : {FirstName.title()} and Last Name : {LastName}")

# Stripping Whitespaces (temporary)

FirstName = "Saianuush"
ReFirstName = "   Saianuush    "
print(f"\n{FirstName == ReFirstName}")
print(FirstName == ReFirstName.rstrip().lstrip())
ReFirstName = ReFirstName.strip()
print(FirstName == ReFirstName)

# Removing Prefix 
print()

URL = "https://Google.com"
print(URL.removeprefix("https://"))
print(URL)
print(URL.removesuffix("Google"))   # nothing happens
print(URL.removesuffix(".com"))