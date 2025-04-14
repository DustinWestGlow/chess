import pygame
from pygame.locals import *
import random
import time

from variables import *
from data import *
from assets import *
from drawing import *
from engine import *

pygame.init()
vec = pygame.math.Vector2

FramePerSec = pygame.time.Clock()


pygame.display.set_caption("Chess")

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