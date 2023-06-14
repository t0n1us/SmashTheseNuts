import pygame, sys

import graphics.menu
from graphics.menu import *
from world.worlds.default1 import Default1
from world.map import Map
from player.player import Player
from player import PlayerManager

WINDOW_DIMSENSION_X = 1400
WINDOW_DIMSENSION_Y = 800
WINDOW_TITLE = "Smash These Nuts"
game_pause = False
FPS = 999

DEBUG_MODE = True

def handle_move(player):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.move_left()
    if keys[pygame.K_RIGHT]:
        player.move_right()
    if keys[pygame.K_UP]:
        player.jump()
    if keys[pygame.K_DOWN]:
        player.move_down()


def handle_gravity(player):  # applies gravity to the player
    if not player.vert_colision:
        player.fall_count += 0.00007
        player.y_vel += player.fall_count
        player.posy += player.y_vel







def run():
    global game_pause
    pygame.init()

    # Window stuff
    window = pygame.display.set_mode((WINDOW_DIMSENSION_X, WINDOW_DIMSENSION_Y))
    pygame.display.set_caption(WINDOW_TITLE)
    window.fill("black")


    # Clock stuff
    clock = pygame.time.Clock()

    # Font stuff
    debug_font = graphics.menu.get_font(18)

    running = True

    players = [Player(window, 400, 50, 40), Player(window, 500, 50, 40, ai_controlled=True)]

    game_map: Map = Default1(window, WINDOW_DIMSENSION_X, WINDOW_DIMSENSION_Y, players)

    while running:
        dt = clock.tick(FPS)  # dt is used to get the relative time difference


        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    graphics.menu.options()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        game_map.render()

        if DEBUG_MODE:
            fps_counter = debug_font.render(f"{clock.get_fps():.0f} fps", False, (89, 89, 0))
            window.blit(fps_counter, (WINDOW_DIMSENSION_X - 100, 20))

        PlayerManager.handle_move(players)
        PlayerManager.handle_gravity(players)

        game_map.vertical_colision_detection()

        pygame.display.flip()  # The only flip we need


if __name__ == "__main__":
    menu()
    pygame.quit()
