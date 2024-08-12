import random
import sys

import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (0, 0, 0)
FRAMES_PER_SECOND = 60

pygame.init()
canvas = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
game_clock = pygame.time.Clock()


def game_loop():
    canvas.blit(player_image, player_rect)


center_height = SCREEN_HEIGHT // 2
player_image = pygame.image.load("../images/player.png").convert_alpha()
player_rect = player_image.get_rect()
player_rect.move_ip(0, center_height)

while True:
    quit_requested = pygame.event.get(eventtype=pygame.QUIT)
    if quit_requested:
        break
    canvas.fill(BACKGROUND_COLOR)
    game_loop()
    pygame.display.flip()
    game_clock.tick(FRAMES_PER_SECOND)
