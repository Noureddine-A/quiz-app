from tkinter import *
import time

THEME_COLOR = "#375362"


class UI:

    def __init__(self, root, quizmanager):
        self.root = root
        self.root.title("Quiz")
        self.root.config(pady=20, padx=20, bg=THEME_COLOR)
        self.quizmanager = quizmanager
        self.canvas = Canvas(root, width=300, height=250, bg="white")
        self.canvas_question = self.canvas.create_text(150, 125, width=280, text=self.quizmanager.get_question(), font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=1, columnspan=2)
        self.score_label = Label(text=f"Score: {0}", background=THEME_COLOR, highlightthickness=0, fg="white")
        self.score_label.grid(row=0, column=2)
        self.correct_img = PhotoImage(file="./images/true.png")
        self.correct_button = Button(image=self.correct_img, command=self.answered_question)
        self.correct_button.grid(column=1, row=2)
        self.false_img = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=self.false_img, command=self.answered_question)
        self.false_button.grid(column=2, row=2)

    def answered_question(self):
        correct = self.quizmanager.check_answer("True")

        question = self.quizmanager.get_question()

        if correct[1] == "True":
            self.score_label.config(text=f"Score: {correct[0]}")
            self.canvas.config(background="green")
        elif correct[1] == "Game over":
            self.root.after(2000, self.reset_canvas, question)
        else:
            self.canvas.config(background="red")

        self.root.after(2000, self.reset_canvas, question)

    def reset_canvas(self, question):
        self.canvas.config(background="white")
        if question == "Game over":
            self.canvas.itemconfig(self.canvas_question, text="You've reached the end.")
            self.correct_button["state"] = "disabled"
            self.false_button["state"] = "disabled"
        else:
            self.canvas.itemconfig(self.canvas_question, text=question)
