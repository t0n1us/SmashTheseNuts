import pygame
from world.default1 import Default1
from player.player import Player
from world.object import Block

WINDOW_DIMSENSION_X = 1400
WINDOW_DIMSENSION_Y = 800
WINDOW_TITLE = "Smash These Nuts"
FPS = 60

GAME_DELAY = 10  # In milliseconds


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


def handle_gravity(player): #applies gravity to the player
    if not player.vert_colision:
        player.fall_count += 0.0006
        player.y_vel += player.fall_count
        player.posy += player.y_vel


def colision_reset(player, block):
    player.set_position(player.posx, block.posy - player.size)
    player.y_vel = 0
    player.fall_count = 0
    player.vert_colision = True


def vertical_colision_detection(players: list[Player], blocks: list[Block]):
    for player in players:
        for blox in blocks:

            if player.posy+player.size+player.y_vel >= blox.posy and player.posy+player.size <= blox.posy:

                # case num.1: the block is directly on the left edge
                if player.right_edge >= blox.posx and player.right_edge <= blox.right_edge:

                    colision_reset(player, blox)

                #case num.2: player is on the right edge of the block
                elif player.posx >= blox.posx and player.posx <= blox.right_edge:

                    colision_reset(player, blox)

                #case num.3: if the block is smaler then the player size
                elif player.posx <= blox.posx and player.right_edge >= blox.right_edge:

                    colision_reset(player, blox)

                else:
                    player.vert_colision = False


def run():

    pygame.init()

    window = pygame.display.set_mode((WINDOW_DIMSENSION_X, WINDOW_DIMSENSION_Y))

    pygame.time.delay(GAME_DELAY)
    pygame.display.set_caption(WINDOW_TITLE)

    running = True

    players = [Player(window, 400, 50, 40)]
    blocks = [Block(window, 250, WINDOW_DIMSENSION_Y-150, 400), Block(window, 300, WINDOW_DIMSENSION_Y - 250, 200)]

    map = Default1(window, WINDOW_DIMSENSION_X, WINDOW_DIMSENSION_Y, players, blocks)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        handle_move(players[0])
        handle_gravity(players[0])
        vertical_colision_detection(players, blocks)

        map.render()
        pygame.display.update()


if __name__ == "__main__":
    run()
    pygame.quit()
