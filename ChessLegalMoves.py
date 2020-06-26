from itertools import permutations 

class Piece:
    def check_valid_position(self, position):
        if position[0] not in range(1,9) or position[1] not in range(1,9):
            raise ValueError('The given position is invalid.')
        return position

    def decode_position(self, position_raw):
        if position_raw[:1].isdigit() or not position_raw[1:].isdigit():
            raise ValueError('The given position is invalid.')
        return self.check_valid_position((ord(position_raw[:1]) - 96, int(position_raw[1:])))

    def encode_position(self, position):
        return str(chr(position[0] + 96) + str(position[1]))

    def is_on_board(self, position):
        return position[0] in range(1,9) and position[1] in range(1,9)

    def moveFilter(self, moves, position):
        #gets all legal moves within boundary
        legal_moves = [move for move in moves if self.is_on_board(tuple(x-y for x,y in zip(position, move)))] #delta of tuples

        #converts move-vectors into positions
        pos = [tuple(x-y for x,y in zip(position, move)) for move in legal_moves]

        #readable positions
        return [self.encode_position(decoded) for decoded in pos]

    def get_decoded_moves(self, moves):
        return [self.decode_position(move) for move in moves]

class Knight(Piece):
    def __init__(self, position_raw):
        self.position_raw = position_raw #str
        self.position = super().decode_position(self.position_raw)
        self.legalMoves = self.getlegalMoves()

    def set_position(self, new_position_raw):
        #Updateing new values
        self.position = super().decode_position(new_position_raw)
        self.legalMoves = self.getlegalMoves()

    def getlegalMoves(self):
        #vector like objects, no positions
        possible_moves = [i for i in list(permutations([1,2,-1,-2], 2)) if abs(i[0]) != abs(i[1])] #deletes repeating moves

        #legal moves -> convert moves into positions -> readable positions
        return super(Knight, self).moveFilter(possible_moves, self.position)


class Bishop(Piece):
    def __init__(self, position_raw):
        self.position_raw = position_raw #str
        self.position = super().decode_position(self.position_raw)
        self.legalMoves = self.getlegalMoves()

    def set_position(self, new_position_raw):
        self.position = super().decode_position(new_position_raw)
        self.legalMoves = self.getlegalMoves()

    def getlegalMoves(self):
        possible_moves = list(dict.fromkeys(list(permutations([1, 1, -1, -1], 2)))) #one step in each direction
        expand = []
        for i in range(2,9):
            for move in possible_moves:
                expand.append((move[0]*i, move[1]*i))
        possible_moves += expand
        return super(Bishop, self).moveFilter(possible_moves, self.position)


class Rook(Piece):
    def __init__(self, position_raw):
        self.position_raw = position_raw #str
        self.position = super().decode_position(self.position_raw)
        self.legalMoves = self.getlegalMoves()

    def set_position(self, new_position_raw):
        self.position = super().decode_position(new_position_raw)
        self.legalMoves = self.getlegalMoves()

    def getlegalMoves(self):
        possible_moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        expand = []
        for i in range(2,9):
            for move in possible_moves:
                expand.append((move[0]*i, move[1]*i))
        possible_moves += expand

        return super(Rook, self).moveFilter(possible_moves, self.position)


class Queen(Piece):
    def __init__(self, position_raw):
        self.position_raw = position_raw #str
        self.position = super().decode_position(self.position_raw)
        self.legalMoves = self.getlegalMoves()

    def set_position(self, new_position_raw):
        self.position = super().decode_position(new_position_raw)
        self.legalMoves = self.getlegalMoves()

    def getlegalMoves(self):
        q_bishop = Bishop(self.position_raw)
        q_rook = Rook(self.position_raw)

        return q_bishop.legalMoves + q_rook.legalMoves


class King(Piece):
    def __init__(self, position_raw):
        self.position_raw = position_raw #str
        self.position = super().decode_position(self.position_raw)
        self.legalMoves = self.getlegalMoves()

    def set_position(self, new_position_raw):
        self.position = super().decode_position(new_position_raw)
        self.legalMoves = self.getlegalMoves()

    def getlegalMoves(self):
        #vector like objects, no positions
        possible_moves = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

        return super(King, self).moveFilter(possible_moves, self.position)


class Pawn(Piece):
    def __init__(self, position_raw, color):
        self.position_raw = position_raw #str
        self.position = super().decode_position(self.position_raw)
        self.color = color
        self.legalMoves = self.getlegalMoves()
        
    def set_position(self, new_position_raw):
        self.position = super().decode_position(new_position_raw)
        self.legalMoves = self.getlegalMoves()

    def getlegalMoves(self):
        if self.color == 'white':
            possible_moves = [(0, -1)]    
        elif self.color == 'black':
            possible_moves = [(0, 1)]
        else:
            raise ValueError('The given color is invalid')

        #2 moves at the beginning
        if self.position[1] in [2, 7]:
            possible_moves.append( (0, possible_moves[0][1] * 2 ))

        return super(Pawn, self).moveFilter(possible_moves, self.position)


