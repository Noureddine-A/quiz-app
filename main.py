from quiz_data import QuizData
from ui import UI
from quiz_manager import QuizManager
from tkinter import *

quiz_data = QuizData()
questions = quiz_data.get_questions()

root = Tk()
quiz_manager = QuizManager(questions)
ui = UI(root, quiz_manager)
root.mainloop()



