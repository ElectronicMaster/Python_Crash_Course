from pathlib import Path

path = Path("D:\GitHub\Python_Crash_Course\Part_1\Chapter_10\Exception_Handling\Alice_In_Wonderland.txt")
content = path.read_text(encoding='utf-8')
lst = content.split()
length = len(lst)
print(f"The file {path} has {length} words")