from pathlib import Path
import json

path = Path("D:\GitHub\Python_Crash_Course\Part_1\Chapter_10\Storing_Data\\numbers.json")
content = path.read_text()
numbers = json.loads(content)
print(numbers)