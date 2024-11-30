import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        
        self.current_player = "X"
        self.winner = False
        
        self.create_widgets()
        self.layout_widgets()

    def create_widgets(self):
        self.buttons = [tk.Button(self.root, text="", font=("normal", 25), width=6, height=2, 
                                command=lambda i=i: self.button_click(i)) for i in range(9)]
        self.label = tk.Label(self.root, text=f"Player {self.current_player}'s turn", font=("normal", 16))

    def layout_widgets(self):
        for i, button in enumerate(self.buttons):
            button.grid(row=i // 3, column=i % 3)
        self.label.grid(row=3, column=0, columnspan=3)

    def button_click(self, index):
        if self.buttons[index]["text"] == "" and not self.winner:
            self.buttons[index]["text"] = self.current_player
            self.check_winner()
            if not self.winner:
                self.toggle_player()

    def check_winner(self):
        winning_combinations = [
            [0,1,2], [3,4,5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]
        ]
        for combo in winning_combinations:
            if self.buttons[combo[0]]["text"] == self.buttons[combo[1]]["text"] == self.buttons[combo[2]]["text"] != "":
                self.buttons[combo[0]].config(bg="green")
                self.buttons[combo[1]].config(bg="green")
                self.buttons[combo[2]].config(bg="green")
                messagebox.showinfo("Tic-Tac-Toe", f"Player {self.buttons[combo[0]]['text']} wins!")
                self.winner = True
                self.root.quit()

    def toggle_player(self):
        self.current_player = "X" if self.current_player == "O" else "O"
        self.label.config(text=f"Player {self.current_player}'s turn")


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
