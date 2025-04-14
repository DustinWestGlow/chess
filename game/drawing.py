import pygame

def color_tile(row, col, color):
    tile = pygame.Rect(tile_size * col, tile_size * (7 - row), tile_size, tile_size)
    pygame.draw.rect(screen, color, tile)
def draw_board():
    # first draw tiles
    flop_colors = [colors['white'], colors['black']]
    turn_color = (255, 255, 150)
    flopper = 0
    for row in range(8):
        for col in range(8):
            flopper = (flopper + 1) % 2 # put left-bottom tile (0, 0) black
            which_color = flop_colors[flopper]
            color_tile(row, col, which_color)
            
        flopper = (flopper + 1) % 2
    # highlight which player's move with tile
    if TURN.color == 'white':
        color_tile(0, 7, turn_color)
    else:
        color_tile(7, 0, turn_color)
    # highlight desired tiles
    if DESIRE == None:
        pass
    else:
        color_tile(DESIRE[0], DESIRE[1], colors['desire'])
    # then draw pieces
    for piece in FOO.pieces:
        draw_piece(piece)
    for piece in BAR.pieces:
        draw_piece(piece)