from pathlib import Path

path = Path('D:\GitHub\Python_Crash_Course\Part_1\Chapter_10\File_Handling\programming.txt')
content = path.read_text()
lines = content.splitlines() # Splits lines into individual parts (into list)

# print(content)

print(lines[0])

for line in lines:
    print(line)