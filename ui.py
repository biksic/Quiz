from tkinter import Tk, Label, Canvas, Button, PhotoImage
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx= 20, pady=20)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas()

        self.question_text = self.canvas.create_text(150, 125, width=280, text="question", font=("Arial", 20, "italic"))
        self.canvas.config(height=250, width=300, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)



        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.click_true)
        self.true_button.grid(column=0, row=2)


        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.click_false)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.question_text, text="End")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def click_true(self):
        ans = self.quiz.check_answer("True")
        self.give_feedback(ans)

    def click_false(self):
        ans = self.quiz.check_answer("False")
        self.give_feedback(ans)


    def give_feedback(self, ans):
        if ans:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)





