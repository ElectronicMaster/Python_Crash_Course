from survey import AnanymousSurvey

question = "What language did you first learn to speak?"
language_survey = AnanymousSurvey(question)

language_survey.showQuestion()

print("Press 'q' anytime to quit.")
while(True):
    response = input("Language : ")
    if response == "q":
        break
    language_survey.store_response(response)

language_survey.showResult()