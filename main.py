import pygame
from world.default1 import Default1
from player.player import Player
from world.object import Block
from itertools import repeat

WINDOW_DIMSENSION_X = 1400
WINDOW_DIMSENSION_Y = 800
WINDOW_TITLE = "Smash These Nuts"

MAP_LIMIT_TOP = -500
MAP_LIMIT_BOTTOM = WINDOW_DIMSENSION_Y + 500
MAP_LIMIT_RIGHT = WINDOW_DIMSENSION_X + 500
MAP_LIMIT_LEFT = -500
FPS = 60

CENTER_X = WINDOW_DIMSENSION_X // 2
CENTER_Y = WINDOW_DIMSENSION_Y // 2

GAME_DELAY = 10  # In milliseconds

OFFSET = repeat((0, 0)) #idk what this does but it is for the screen shake


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
        player.fall_count += 0.00007
        player.y_vel += player.fall_count
        player.posy += player.y_vel
        print('hello')

def arrow_direction(window, player):

    origine = (CENTER_X, CENTER_Y)
    end_pos = (player.posx, player.posy)

    pygame.draw.line(window, (0, 0, 0), origine, end_pos, width=5)


#Return True if the player is out boundries or of the window (return false if player is visible)
def handle_limits(window, player): #respawn player if he touches the outside limit (and play animation) (show arrow when player is not visible)

    if player.posy < 0 or player.posy > WINDOW_DIMSENSION_Y: #check if player is outside visible window in Y

        if player.posy >= MAP_LIMIT_BOTTOM or player.posy <= MAP_LIMIT_TOP:
            player.set_position(700, 100)
            global OFFSET
            OFFSET = screen_shake(5, 40)

        else: # player not out but not visible (display an arrow)
            arrow_direction(window, player)
            '''pygame.draw.polygon(window, (0, 0, 0),
                                ((0, 100), (0, 200), (200, 200), (200, 300), (300, 150), (200, 0), (200, 100)))'''

    elif player.posx < 0 or player.posx > WINDOW_DIMSENSION_X: #check if player is outside visible window in X

        if player.posx >= MAP_LIMIT_RIGHT or player.posx <= MAP_LIMIT_LEFT:
            player.set_position(700, 100)
            OFFSET = screen_shake(5, 40)

        else: # player not out but not visible (display an arrow)
            arrow_direction(window, player)
            '''pygame.draw.polygon(window, (0, 0, 0),
                                ((0, 100), (0, 200), (200, 200), (200, 300), (300, 150), (200, 0), (200, 100)))'''
    else:
        return False


def vertical_colision_detection(players: list[Player], blocks: list[Block], window):
    for player in players:
        #check is player is out of the map

        handle_limits(window, player)

        '''if player.posy >= MAP_LIMIT_BOTTOM or player.posy <= MAP_LIMIT_TOP: #Mettre cette section si dans une fonction appart (would be clean)
            player.set_position(700, 100)
            global OFFSET
            OFFSET = screen_shake(5, 40)

        elif player.posx >= MAP_LIMIT_RIGHT or player.posx <= MAP_LIMIT_LEFT:
            player.set_position(20, 100)
            OFFSET = screen_shake(700, 40)'''

        for blox in blocks:

            if player.posy+player.size+player.y_vel >= blox.posy and player.posy+player.size <= blox.posy:

                # case num.1: the block is directly on the left edge
                if player.right_edge >= blox.posx and player.right_edge <= blox.right_edge:

                    player.colision_reset(blox)
                    break

                #case num.2: player is on the right edge of the block
                elif player.posx >= blox.posx and player.posx <= blox.right_edge:

                    player.colision_reset(blox)
                    break

                #case num.3: if the block is smaler then the player size
                elif player.posx <= blox.posx and player.right_edge >= blox.right_edge:

                    player.colision_reset(blox)
                    break

                else:
                    player.vert_colision = False


def screen_shake(intensity, amplitude):
    s = -1
    for i in range(0, 15):
        for x in range(0, amplitude, intensity):
            yield x * s, 0
        for x in range(amplitude, 0, intensity):
            yield x * s, 0
        s *= -1
    while True:
        yield 0, 0

def run():

    pygame.init()

    #window = pygame.display.set_mode((WINDOW_DIMSENSION_X, WINDOW_DIMSENSION_Y))
    SHAKE_WINDOW = pygame.display.set_mode((WINDOW_DIMSENSION_X, WINDOW_DIMSENSION_Y))
    window = SHAKE_WINDOW.copy()

    pygame.time.delay(GAME_DELAY)
    pygame.display.set_caption(WINDOW_TITLE)

    running = True

    players = [Player(window, 400, 50, 40)]
    blocks = [Block(window, 250, WINDOW_DIMSENSION_Y-100, 900),
              Block(window, 300, WINDOW_DIMSENSION_Y - 350, 200),
              Block(window, 800, WINDOW_DIMSENSION_Y - 350, 200),
              Block(window, 450, WINDOW_DIMSENSION_Y - 500, 400)]

    map = Default1(window, WINDOW_DIMSENSION_X, WINDOW_DIMSENSION_Y, players, blocks)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        handle_move(players[0])
        handle_gravity(players[0])
        vertical_colision_detection(players, blocks, SHAKE_WINDOW)

        map.render()
        SHAKE_WINDOW.blit(window, next(OFFSET))
        pygame.display.update()


if __name__ == "__main__":
    run()
    pygame.quit()
