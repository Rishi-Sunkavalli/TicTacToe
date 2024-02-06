import tkinter as tk

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.current_player = "X"
        self.game_board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(master, text='-', font=('Arial', 60), width=4, height=2,
                                   command=lambda i=i, j=j: self.click_button(i, j))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

    def click_button(self, row, col):
        button = self.buttons[row][col]
        if button['text'] == '-':
            button['text'] = self.current_player
            self.game_board[row][col] = self.current_player
            if self.check_win(row, col):
                self.show_message(f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.check_tie():
                self.show_message("Tie game!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_win(self, row, col):
        # Check row
        if self.game_board[row][0] == self.game_board[row][1] == self.game_board[row][2] != '-':
            return True
        # Check column
        if self.game_board[0][col] == self.game_board[1][col] == self.game_board[2][col] != '-':
            return True
        # Check diagonal
        if row == col and self.game_board[0][0] == self.game_board[1][1] == self.game_board[2][2] != '-':
            return True
        if row + col == 2 and self.game_board[0][2] == self.game_board[1][1] == self.game_board[2][0] != '-':
            return True
        return False

    def check_tie(self):
        for i in range(3):
            for j in range(3):
                if self.game_board[i][j] == '-':
                    return False
        return True

    def show_message(self, message):
        popup = tk.Toplevel()
        popup.title("Game Over")
        label = tk.Label(popup, text=message, font=('Arial', 20))
        label.pack(padx=50, pady=50)
        button = tk.Button(popup, text="Restart", font=('Arial', 20), command=self.reset_game)
        button.pack(padx=50, pady=50)

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]['text'] = '-'
                self.game_board[i][j] = '-'
        self.current_player = "X"

if __name__ == '__main__':
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()