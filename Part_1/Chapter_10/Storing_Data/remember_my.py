from pathlib import Path
import json

path = Path("Part_1/Chapter_10/Storing_Data/username.json")

username = input("Whats you'r name? ")
content = json.dumps(username)
path.write_text(content)
print(f"We will remember you, {username}")

if(path.exists()):
    content = path.read_text()
    usernameInJSON = json.loads(content)
    print(f"Welcome back, {usernameInJSON}")
else:
    username = input("Whats you'r name? ")
    content = json.dumps(username)
    path.write_text(content)
    print(f"We will remember you, {username}")