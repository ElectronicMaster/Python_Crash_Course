import sys
import os

folder = os.path.abspath('D:\GitHub\Python_Crash_Course\Part_1\Chapter_11')
sys.path.insert(0,folder)

from name_function import get_formatted_name

def test_first_last_name():
    formatted_name = get_formatted_name("sai","anuush")
    assert formatted_name == "Sai Anuush"

def test_first_middle_last_name():
    formatted_name = get_formatted_name("sai","M.A.","anuush")
    assert formatted_name == "Sai Anuush M.A."

# single . shows that the function has passed all test cases
# F represents the test has been failed