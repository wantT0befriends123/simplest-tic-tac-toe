
class Minimax:
    @staticmethod
    def minimax(board, is_maximizing):
        # Minimax algorithm to determine the best move for the computer
        winner = Minimax.check_winner_simulated(board)
        if winner == "X":
            return -1
        elif winner == "O":
            return 1
        elif "-" not in board:
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for i in range(9):
                if board[i] == "-":
                    board[i] = "O"
                    score = Minimax.minimax(board, False)
                    board[i] = "-"
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(9):
                if board[i] == "-":
                    board[i] = "X"
                    score = Minimax.minimax(board, True)
                    board[i] = "-"
                    best_score = min(score, best_score)
            return best_score

    @staticmethod
    def check_winner_simulated(board):
        # Check if there is a winner or a tie on a simulated board
        winning_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        for combination in winning_combinations:
            if board[combination[0]] == board[combination[1]] == board[combination[2]] != "-":
                return board[combination[0]]
        if "-" not in board:
            return "Tie"
        return None