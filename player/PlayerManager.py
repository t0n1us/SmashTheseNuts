import pygame
from player.player import Player


def handle_move(players: list[Player]):
    for player in players:

        if player.is_ai_controlled:
            continue

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player.move_left()
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player.move_right()
        if keys[pygame.K_UP] or keys[pygame.K_w] or keys[pygame.K_SPACE]:
            player.jump()
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            player.move_down()


def handle_gravity(players: list[Player]):  # applies gravity to the player
    for player in players:
        if not player.vert_colision:
            player.fall_count += 0.00007
            player.y_vel += player.fall_count
            player.posy += player.y_vel
