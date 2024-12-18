import os
import sys

path = os.path.abspath("D:\GitHub\Python_Crash_Course\Part_1\Chapter_11\\test")
sys.path.insert(0,path)

from survey import AnanymousSurvey
import pytest

@pytest.fixture
def test_store_single_response():
    question = "What languages did you first learn to speak?"
    language_survey = AnanymousSurvey(question)
    responses = ["English","Spanish","Mandarin"]
    for response in responses:
        language_survey.store_response(response)
    for response in responses:
        assert response in language_survey.responses