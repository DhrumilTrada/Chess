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

    def print_board(self):
        for row in self.board:
            print(' '.join(row))
        print()

    def is_valid_move(self, start, end):
        if not (0 <= start[0] < 8 and 0 <= start[1] < 8 and 0 <= end[0] < 8 and 0 <= end[1] < 8):
            return False

        piece = self.board[start[0]][start[1]]
        target_piece = self.board[end[0]][end[1]]

        if piece == ' ' or (self.current_player == 'white' and piece.islower()) or (self.current_player == 'black' and piece.isupper()):
            return False

        

        return True

    def move_piece(self, start, end):
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
    #File(a-h)
    #Rank(1-8)
        
        square=input("Enter the square")
        file=square[0].lower()
        rank=int(square[1])
        fileReal=ord(file)-ord('a')
        rankReal=8-rank
        
        square1=input("Enter the square")
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
