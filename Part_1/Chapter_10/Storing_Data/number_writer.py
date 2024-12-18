from pathlib import Path
import json

numbers = [2,3,5,7,11,13]

path = Path('D:\GitHub\Python_Crash_Course\Part_1\Chapter_10\Storing_Data\\numbers.json')
contents = json.dumps(numbers)
path.write_text(contents)