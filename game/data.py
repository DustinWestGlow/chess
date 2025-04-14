class Player():
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.pieces = []
        pawn_row = generation['pawn_row'][color]
        for col in range(8):
            self.pieces.append(
                Piece(name, 'pawn', (pawn_row, col))
            )
        special_row = generation['special_row'][color]
        for col in range(8):
            self.pieces.append(
                Piece(name, generation['piece_order'][col], (special_row, col))
            )


class Piece(pygame.sprite.Sprite):
    def __init__(self, owner, piece, position):
        super().__init__()
        self.owner = owner
        self.piece = piece
        self.position = position
    def console(self):
        print(self.owner, self.piece, self.position)