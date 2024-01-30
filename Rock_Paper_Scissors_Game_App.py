import random
import tkinter as tk
from tkinter import ttk, messagebox

class RockPaperScissorsGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Rock-Paper-Scissors Game")
        self.master.geometry("400x500")
        self.master.configure(bg='lightblue')

        self.user_score = 0
        self.computer_score = 0

        self.create_widgets()

    def create_widgets(self):
        self.user_choice_var = tk.StringVar()

        ttk.Button(self.master, text="Rock", command=lambda: self.play_game("Rock")).pack(pady=10)
        ttk.Button(self.master, text="Paper", command=lambda: self.play_game("Paper")).pack(pady=10)
        ttk.Button(self.master, text="Scissors", command=lambda: self.play_game("Scissors")).pack(pady=10)

        # Create space between lines
        ttk.Label(self.master, text="", background='lightblue').pack(pady=10)

        self.result_label = ttk.Label(self.master, text="", font=('Arial', 14, 'bold'), background='lightblue')
        self.result_label.pack(pady=10)

        self.score_label = ttk.Label(self.master, text="Score: User - 0, Computer - 0", font=('Arial', 14), background='lightblue')
        self.score_label.pack(pady=10)

        ttk.Button(self.master, text="Play Again", command=self.reset_game).pack(pady=20)

    def play_game(self, user_choice):
        computer_choice = random.choice(["Rock", "Paper", "Scissors"])
        result = self.determine_winner(user_choice, computer_choice)
        self.display_result(user_choice, computer_choice, result)
        self.update_score(result)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "Tie"
        elif (
            (user_choice == "Rock" and computer_choice == "Scissors") or
            (user_choice == "Scissors" and computer_choice == "Paper") or
            (user_choice == "Paper" and computer_choice == "Rock")
        ):
            return "User Wins"
        else:
            return "Computer Wins"

    def display_result(self, user_choice, computer_choice, result):
        result_text = f"User Choice: {user_choice}\nComputer Choice: {computer_choice}\nResult: {result}"
        self.result_label.config(text=result_text)

    def update_score(self, result):
        if result == "User Wins":
            self.user_score += 1
        elif result == "Computer Wins":
            self.computer_score += 1

        score_text = f"Score: User - {self.user_score}, Computer - {self.computer_score}"
        self.score_label.config(text=score_text)

    def reset_game(self):
        self.user_score = 0
        self.computer_score = 0
        self.result_label.config(text="")
        self.score_label.config(text="Score: User - 0, Computer - 0")

def main():
    root = tk.Tk()
    app = RockPaperScissorsGame(root)

    # Configure button style
    style = ttk.Style()
    style.configure('TButton', font=('Arial', 14, 'bold'), foreground='black', background='blue', padding=(10, 10))

    root.mainloop()

if __name__ == "__main__":
    main()
