import random
import sys

import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (0, 0, 0)
FRAMES_PER_SECOND = 60
ENEMY_SPEED = 3

pygame.init()
canvas = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
game_clock = pygame.time.Clock()


def create_enemy():
    new_enemy_rect = enemy_image.get_rect()
    start_y = get_random_y(new_enemy_rect.height)
    new_enemy_rect.move_ip(SCREEN_WIDTH, start_y)
    return new_enemy_rect


def game_loop():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_rect.move_ip(0, -1)
    if keys[pygame.K_DOWN]:
        player_rect.move_ip(0, 1)
    if keys[pygame.K_LEFT]:
        player_rect.move_ip(-1, 0)
    if keys[pygame.K_RIGHT]:
        player_rect.move_ip(1, 0)
    canvas.blit(player_image, player_rect)

    global enemy_rect
    enemy_rect.move_ip(-ENEMY_SPEED, 0)
    if enemy_rect.x + enemy_rect.width < 0:
        enemy_rect = create_enemy()

    if player_rect.colliderect(enemy_rect):
        pygame.quit()
        print("Game over!")
        sys.exit()

    canvas.blit(enemy_image, enemy_rect)


def get_random_y(image_height):
    return random.randint(0, SCREEN_HEIGHT - image_height)


center_height = SCREEN_HEIGHT // 2
player_image = pygame.image.load("../images/player.png").convert_alpha()
player_rect = player_image.get_rect()
player_rect.move_ip(0, center_height)

enemy_image = pygame.image.load("../images/lameenemy.png").convert_alpha()
enemy_rect = create_enemy()

while True:
    quit_requested = pygame.event.get(eventtype=pygame.QUIT)
    if quit_requested:
        break
    canvas.fill(BACKGROUND_COLOR)
    game_loop()
    pygame.display.flip()
    game_clock.tick(FRAMES_PER_SECOND)
