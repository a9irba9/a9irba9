import tkinter as tk
from tkinter import messagebox
import random

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")

        self.current_question = None
        self.current_answer = None
        self.load_questions()

        self.question_label = tk.Label(root, text="Welcome to the Quiz Game!", wraplength=400)
        self.question_label.pack(pady=20)

        self.answer_entry = tk.Entry(root)
        self.answer_entry.pack(pady=10)

        self.submit_button = tk.Button(root, text="Submit Answer", command=self.check_answer)
        self.submit_button.pack(pady=10)

        self.next_button = tk.Button(root, text="Next Question", command=self.next_question)
        self.next_button.pack(pady=10)

        self.next_question()  # Load the first question

    def load_questions(self):
        """Load questions and answers from a file."""
        self.questions_and_answers = []
        try:
            with open("questions.txt", "r") as file:
                for line in file:
                    if '=' in line:
                        question, answer = line.strip().split('=', 1)
                        self.questions_and_answers.append((question, answer))
        except FileNotFoundError:
            messagebox.showerror("Error", "Questions file not found.")
            self.root.quit()
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.root.quit()

    def next_question(self):
        """Display the next question."""
        self.answer_entry.delete(0, tk.END)  # Clear the answer entry
        if self.questions_and_answers:
            question, answer = random.choice(self.questions_and_answers)  # Choose a random question
            self.current_question = question
            self.current_answer = answer
            self.question_label.config(text=question)
        else:
            self.question_label.config(text="No questions available.")

    def check_answer(self):
        """Check the user's answer and display the result."""
        user_answer = self.answer_entry.get().strip()
        if user_answer.lower() == self.current_answer.lower():
            messagebox.showinfo("Correct!", "Your answer is correct!")
        else:
            messagebox.showerror("Incorrect", f"Sorry, the correct answer was: {self.current_answer}")

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
