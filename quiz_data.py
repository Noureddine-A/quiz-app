import requests
import html


class QuizData:

    def __init__(self):
        self.questions = []

    def get_questions(self):
        response = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
        json = response.json()
        results = json["results"]

        for question in results:
            question_dict = {
                "question": html.unescape(question["question"]),
                "correct_answer": html.unescape(question["correct_answer"])
            }
            self.questions.append(question_dict)

        return self.questions



