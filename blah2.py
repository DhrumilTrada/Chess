class Chess:
    def __init__(self):
        self.board = [
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        ]
        self.current_player = 'white'
        self.castling = {'white': {'king_side': True, 'queen_side': True},
                         'black': {'king_side': True, 'queen_side': True}}
        self.en_passant_target = None

    def print_board(self):
        for row in self.board:
            print(' '.join(row))
        print()
    def is_valid_knight_move(self, start, end):

        row_diff = abs(end[0] - start[0])
        col_diff = abs(end[1] - start[1])

        return (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2)

    def is_valid_bishop_move(self, start, end):
        row_diff = abs(end[0] - start[0])
        col_diff = abs(end[1] - start[1])

        return row_diff == col_diff
    
    def is_valid_rook_move(self, start, end):
        return start[0] == end[0] or start[1] == end[1]
    
    def is_valid_pawn_move(self, start, end):
        direction = -1 if self.current_player == 'white' else 1

        # Regular pawn move (one square forward)
        print("Test1")
        if start[1] == end[1] and start[0] + direction == end[0]:
            print("Test2")

            return self.board[end[0]][end[1]] == ' '

        # Initial double move for pawns
        elif start[1] == end[1] and abs(start[0] + 2 * direction) == end[0] and \
                ((start[0] == 6 and self.current_player == 'white') or
                 (start[0] == 1 and self.current_player == 'black')) and \
                self.board[end[0]][end[1]] == ' ' and self.board[start[0] + direction][start[1]] == ' ':
            print("Test3")

            return True

        # Pawn capture (diagonal)
        elif abs(start[1] - end[1]) == 1 and start[0] + direction == end[0]:
            target_piece = self.board[end[0]][end[1]]
            print("Test4")

            return target_piece.islower() if self.current_player == 'white' else target_piece.isupper()

        return False
    
    def is_valid_queen_move(self, start, end):
        row_diff = abs(end[0] - start[0])
        col_diff = abs(end[1] - start[1])

        return (start[0] == end[0] or start[1] == end[1]) or (row_diff == col_diff)
    
    def is_valid_king_move(self, start, end):
        row_start, col_start = start
        row_end, col_end = end
        piece = self.board[row_start][col_start]

        # Check if the move is one square in any direction
        row_diff = abs(row_end - row_start)
        col_diff = abs(col_end - col_start)

        # Regular move
        if row_diff <= 1 and col_diff <= 1:
            return True

        # Castling (to be implemented separately)
        # Add conditions for castling, such as checking if the king and rook haven't moved

        return False
    
    def is_valid_move(self, start, end):
        piece = self.board[start[0]][start[1]]
        target_piece = self.board[end[0]][end[1]]
        if not (0 <= start[0] < 8 and 0 <= start[1] < 8 and 0 <= end[0] < 8 and 0 <= end[1] < 8):
            return False
        if piece=='N' or piece=='n' :
            if(not self.is_valid_knight_move(start, end)):
                return False
        if piece=='B' or piece=='b' :
            if(not self.is_valid_bishop_move(start, end)):
                return False
        if piece=='R' or piece=='r' :
            if(not self.is_valid_rook_move(start, end)):
                return False
        if piece=='P' or piece=='p' :
            if(not self.is_valid_pawn_move(start, end)):
                return False
        if piece=='Q' or piece=='q' :
            if(not self.is_valid_queen_move(start, end)):
                return False
        if piece=='K' or piece=='k' :
            if(not self.is_valid_king_move(start, end)):
                return False
        

        if piece == ' ' or (self.current_player == 'white' and piece.islower()) or (self.current_player == 'black' and piece.isupper()):
            return False

        return True

    def move_piece(self, start, end):
        # if self.is_valid_move(start, end):
        #     piece = self.board[start[0]][start[1]]
        #     target_piece = self.board[end[0]][end[1]]

        #     if piece.lower() == 'p':
        #         # Handle pawn move separately
        #         pass
        #     elif piece.lower() == 'n':
        #         # Handle knight move separately
        #         pass
        #     elif piece.lower() == 'b':
        #         # Handle bishop move separately
        #         pass
        #     elif piece.lower() == 'r':
        #         # Handle rook move separately
        #         pass
        #     elif piece.lower() == 'q':
        #         # Handle queen move separately
        #         pass
        #     elif piece.lower() == 'k':
        #         # Handle king move separately
        #         pass

        #     self.switch_player()
        #     return True
        # else:
        #     return False
        if self.is_valid_move(start, end):
            piece = self.board[start[0]][start[1]]
            self.board[start[0]][start[1]] = ' '
            self.board[end[0]][end[1]] = piece
            self.switch_player()
            return True
        else:
            return False

    def switch_player(self):
        if self.current_player == 'white':
            self.current_player = 'black'
        else:
            self.current_player = 'white'


if __name__ == "__main__":
    chess_game = Chess()

    while True:
        chess_game.print_board()
        print(f"{chess_game.current_player.capitalize()}'s turn")

        square=input("Enter the square : ")
        file=square[0].lower()
        rank=int(square[1])
        fileReal=ord(file)-ord('a')
        rankReal=8-rank
        
        square1=input("Enter the square : ")
        file1=square1[0].lower()
        rank1=int(square1[1])
        fileReal1=ord(file1)-ord('a')
        rankReal1=8-rank1

        # start_col = int(input("Enter the starting column (0-7): "))
        # start_row = int(input("Enter the starting row (0-7): "))
        # end_col = int(input("Enter the ending column (0-7): "))
        # end_row = int(input("Enter the ending row (0-7): "))

        move_result = chess_game.move_piece((rankReal, fileReal), (rankReal1, fileReal1))

        if not move_result:
            print("Invalid move. Try again.")
