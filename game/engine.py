from variables import *
import pygame
from drawing import *

PICKED = None
PLAYERS = [FOO, BAR]
TURN = PLAYERS[0]

def get_picked():
    return PICKED
def get_players():
    return PLAYERS
def get_turn():
    return TURN

def frontier(player):
    return
def valid_move(piece, tile):
    if piece == None:
        return False
    return True
    # return [(0, 0)]

click_grid = (-1, -1)
click_reset = True

# Input is a tuple: (x, y) in pixels the cursor coordinates
# Output a tuple: (row, col) of the tile containing cursor
# Cursor position -> corresponding Tile
def to_grid(pos):
    col = pos[0] // tile_size
    row = 7 - (pos[1] // tile_size)
    return (row, col)

# Input is a Tile tuple: (row, col)
# Output is a Piece instance or None
# If the input tile has a chess piece on it, return that piece
# (specifically a chess piece of the current player)
# otherwise, return None 
# which Tile -> Piece instance or None
def is_yours(tile):
    for piece in TURN.pieces:
        if piece.position == tile:
            return True
    return False

def get_piece(tile):
    for player in PLAYERS:
        for piece in player.pieces:
            if piece.position == tile:
                return piece
    return None

def handle_click(pos):
    color_tile(pos[0], pos[1], colors['desire'])

first_frame = True
def update():
    global first_frame
    global PICKED
    pygame.event.get()
    mousedown = pygame.mouse.get_pressed()[0]
    if mousedown and first_frame:
        first_frame = False
        clicked_tile = to_grid(pygame.mouse.get_pos())
        in_your_pieces = is_yours(clicked_tile)
        picked_piece = get_piece(clicked_tile)
        PICKED = picked_piece
        # PICKED.console()
        # print(in_your_pieces)
        if not in_your_pieces:
            PICKED = None
            if valid_move(PICKED, clicked_tile):
                PICKED = None
                PICKED.move(clicked_tile)
    else:
        first_frame = True

