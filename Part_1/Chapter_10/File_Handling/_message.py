from pathlib import Path

content = "I love programming\n"
content += "I love creating new games\n"
content += "I also working with data\n"

path = Path('D:\GitHub\Python_Crash_Course\Part_1\Chapter_10\File_Handling\programming.txt')
path.write_text(content)