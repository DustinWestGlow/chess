from variables import *
import pygame
from drawing import *

def record_positions():
    global piece_position_list
    counted = []
    for player in PLAYERS:
        for piece in player.pieces:
            counted.append(piece.position)
    piece_position_list = counted
    print(counted)
def move_piece(piece, position):
    piece.position = position
    record_positions()

def frontier(player):
    return
def valid_moves(piece):
    if piece == None:
        return None
    return [(0, 0)]

click_grid = (-1, -1)
click_reset = True
def to_grid(pos):
    col = pos[0] // tile_size
    row = 7 - (pos[1] // tile_size)
    return (row, col)
def find_piece(tile):
    for piece in TURN.pieces:
        if piece.position == tile:
            return piece.piece
    return None
def update():
    global click_reset
    global DESIRE
    pygame.event.get()
    if pygame.mouse.get_pressed()[0] == True:
        if click_reset == True:
            clicked_tile = to_grid(pygame.mouse.get_pos())
            clicked_piece = find_piece(clicked_tile)
            # if piece is clicked
            if clicked_piece is not None:
            # if clicked_tile in piece_position_list:
                DESIRE = clicked_tile
            # else if empty space is clicked
            else:
                # if player is trying to move a piece
                print(valid_moves(DESIRE))
                if DESIRE and valid_moves(DESIRE) and clicked_tile in valid_moves(DESIRE):
                    move_piece(DESIRE, clicked_tile)
                # else, player is clicking-off, so de-highlight
                DESIRE = None
            click_reset = False
    else:
        click_reset = True
def handle_click(pos):
    color_tile(pos[0], pos[1], colors['desire'])