import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (0, 0, 0)
FRAMES_PER_SECOND = 60

pygame.init()
canvas = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
game_clock = pygame.time.Clock()


def game_loop():
    pass


## Hier initialiseren we de speler en de vijand
## player_image = ...


while True:
    quit_requested = pygame.event.get(eventtype=pygame.QUIT)
    if quit_requested:
        break
    canvas.fill(BACKGROUND_COLOR)
    game_loop()
    pygame.display.flip()
    game_clock.tick(FRAMES_PER_SECOND)
