import time, os
from minimax import Minimax

class Board():
    def __init__(self):
        # Initialize the board with empty cells
        self.board = ["-", "-", "-",
                      "-", "-", "-",
                      "-", "-", "-",]

    def clear(self):
        # Clear the screen
        #os.system('cls')  # On Windows
        os.system("clear") #On Mac and Linux System

    def print_board(self):
        # Print the board in a readable format
        rows = ["A", "B", "C"]
        
        print("    1 2 3") # Print column numbers
        print("  +-------+", end = "") # Print top border
        for i in range(0, 9): # Print rows
            if i % 3 == 0: # Print row letters
                print() # New line
                print(rows[(i)//3], end = " | ") # Print row letter and left border

            print(self.board[i], end=" ") # Print board value

            if i % 3 == 2: # Print right border
                print("|", end = "")

        print("\n  +-------+")

    def make_move(self, position, marker):
        # Make a move on the board if the position is valid
        if self.board[position] == "-" and marker in ["X", "O"]:
            self.board[position] = marker
            return True
        else:
            return False
        
    def check_winner(self):
        # Check if there is a winner or a tie
        winning_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        for combination in winning_combinations:
            if self.board[combination[0]] == self.board[combination[1]] == self.board[combination[2]] != "-":
                self.print_board()
                input(f"{self.board[combination[0]]} wins!")
                self.mainmenu()
        if "-" not in self.board:
            self.print_board()
            input("It's a tie!")
            self.mainmenu()
        return None

    def player_input(self):
        # Get input from the player and make a move
        while True:
            position = input("Enter position (eg. A1): \n")
            if len(position) == 2 and position[0].upper() in ["A", "B", "C"] and position[1] in ["1", "2", "3"]:
                row = ["A", "B", "C"].index(position[0].upper())
                col = int(position[1]) - 1
                if self.make_move(row * 3 + col, "X"):
                    break
                else:
                    print("\nInvalid move\n")
            else:
                print("\nInvalid input\n")

    def computer_input(self):
        # Determine the best move for the computer and make the move
        best_score = -float('inf')
        best_move = None
        for i in range(9):
            if self.board[i] == "-":
                self.board[i] = "O"
                score = Minimax.minimax(self.board[:], False)
                self.board[i] = "-"
                if score > best_score:
                    best_score = score
                    best_move = i
        self.make_move(best_move, "O")
        return "Computer moves to " + (["A", "B", "C"][best_move // 3] + str(best_move % 3 + 1)) + ".\n"

    def reset_board(self):
        # Reset the board
        self.board = ["-", "-", "-",
                      "-", "-", "-",
                      "-", "-", "-",]

    def mainmenu(self):
        self.clear()
        # Main menu
        self.reset_board()
        while True:
            print("Tic Tac Toe")
            print("1. Computer")
            print("2. Two player")
            choice = input("\nEnter choice: ")
            if choice == "1":
                self.play_computer()
            elif choice == "2":
                self.play_friend()
            else:
                print("\nInvalid input\n")

    def play_computer(self):
        self.clear()
        # Main game loop
        while True:
            self.print_board()
            time.sleep(0.5)
            self.check_winner()
            self.player_input()
            if self.check_winner() == "X":
                print("Player wins!")
                break
            self.print_board()
            time.sleep(0.5)
            self.check_winner()
            print(self.computer_input())
            time.sleep(0.5)
            if self.check_winner() == "O":
                print("Computer wins!")
                break

    def play_friend(self):
        self.clear()
        # Main game loop
        while True:
            self.print_board()
            self.check_winner()
            self.player_input()
            if self.check_winner() == "X":
                print("Player 1 wins!")
                break
            self.print_board()
            self.check_winner()
            self.player_input()
            if self.check_winner() == "O":
                print("Player 2 wins!")
                break


board = Board()
board.mainmenu()