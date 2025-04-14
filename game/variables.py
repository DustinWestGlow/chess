import pygame
from data import *



# 8 tiles x 8 tiles
# each tile is 64x64 pixels
tile_size = 64
piece_size = 54
HEIGHT = tile_size * 8
WIDTH = tile_size * 8
FPS = 10
FFF = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

generation = {
    'pawn_row': {
        'white': 1,
        'black': 6
    },
    'special_row': {
        'white': 0,
        'black': 7
    },
    'order': ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook']
}

player_hash = {
    'foo': 'white',
    'bar': 'black'
}

images = dict()

colors = {
    'desire': (15, 100, 255),
    'white': (230, 232, 195),
    'black': (92, 140, 70),
}

piece_position_list = []

FOO = Player('foo', 'white')
BAR = Player('bar', 'black')
PLAYERS = [FOO, BAR]
TURN = PLAYERS[0]
DESIRE = None