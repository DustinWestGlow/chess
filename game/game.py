import pygame
from pygame.locals import *
import random
import time

from variables import *
from data import *
from assets import *

pygame.init()
vec = pygame.math.Vector2

FramePerSec = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")

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





def draw_piece(piece):
    # https://stackoverflow.com/questions/8873219/how-can-i-draw-images-and-sprites-in-pygame
    img_key = player_hash[piece.owner] + '_' + piece.piece
    image_surface = images[img_key]
    # the data is represented correctly in the arrays
    # but I'm a noob at flipping the canvas
    row = (7 - piece.position[0]) # 8 - row because of canvas being top-down
    col = piece.position[1]
    x = ((tile_size - piece_size)// 2) + (col * piece_size) + ((tile_size - piece_size) * col)
    y = ((tile_size - piece_size)// 2) + (row * piece_size) + ((tile_size - piece_size) * row)
    screen.blit(image_surface, (x, y))
    return


FOO = Player('foo', 'white')
BAR = Player('bar', 'black')
PLAYERS = [FOO, BAR]
TURN = PLAYERS[0]
DESIRE = None

# move_piece(FOO.pieces[0], (3, 3))

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

DEBUG = False
def main():
    generate_piece_images(images, piece_size)
    record_positions()
    while True and not DEBUG:
        screen.fill(FFF)
        update()
        draw_board()
        pygame.display.update()
        FramePerSec.tick(FPS)
    pygame.quit()


if __name__ == '__main__':
    main()