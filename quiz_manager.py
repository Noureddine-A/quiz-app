class QuizManager:

    def __init__(self, questions):
        self.questions = questions
        self.question_number = 0
        self.score = 0

    def get_question(self):
        if self.question_number < 10:
            question = self.questions[self.question_number]
            return question["question"]
        else:
            return "Game over"

    def check_answer(self, answer_given):
        self.question_number += 1
        if answer_given == self.questions[self.question_number - 1]["correct_answer"]:
            self.score += 1
            return self.score, "True"
        else:
            return self.score, "False"
