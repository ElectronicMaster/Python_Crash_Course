class AnanymousSurvey:
    def __init__(self,question):
        self.question = question
        self.responses = []

    def showQuestion(self):
        print(self.question)
    
    def store_response(self,response):
        self.responses.append(response)
    
    def showResult(self):
        print("Thank you to everyone who participated in the survey")
        print("Survey Result :")
        for response in self.responses:
            print(f" - {response}")