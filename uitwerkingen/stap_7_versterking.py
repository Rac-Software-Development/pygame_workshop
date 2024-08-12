import random
import sys

import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (0, 0, 0)
FRAMES_PER_SECOND = 60
ENEMY_SPEED = 3
ENEMY_SPAWN_RATE = 10

pygame.init()
canvas = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
game_clock = pygame.time.Clock()


def create_enemy():
    enemy_rect = enemy_image.get_rect()
    start_y = get_random_y(enemy_rect.height)
    enemy_rect.move_ip(SCREEN_WIDTH, start_y)
    return enemy_rect


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

    if random.randint(0, 100) < ENEMY_SPAWN_RATE:
        enemies_list.append(create_enemy())

    for enemy_rect in enemies_list:
        enemy_rect.move_ip(-ENEMY_SPEED, 0)
        if enemy_rect.x + enemy_rect.width < 0:
            enemies_list.remove(enemy_rect)

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
enemies_list = []

while True:
    quit_requested = pygame.event.get(eventtype=pygame.QUIT)
    if quit_requested:
        break
    canvas.fill(BACKGROUND_COLOR)
    game_loop()
    pygame.display.flip()
    game_clock.tick(FRAMES_PER_SECOND)
