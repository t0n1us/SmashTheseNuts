from abc import ABC, abstractmethod
import pygame
from player.player import Player
from world.objects.block import Block
from itertools import repeat


class Map(ABC):
    EDGE_WIDTH = 100
    WINDOW_BACKGROUND_COLOR = (199, 125, 255)
    PLATFORM_COLOR = (90, 24, 154)
    BLOCKS = list[Block]

    MAP_LIMIT_TOP = -500
    MAP_LIMIT_BOTTOM = -1  # Cannot set a value without the window size
    MAP_LIMIT_RIGHT = -1  # Cannot set a value without the window size
    MAP_LIMIT_LEFT = -500

    CENTER_X = -1  # Cannot set a value without the window size
    CENTER_Y = -1  # Cannot set a value without the window size

    GRAVITY = -1  # px per seconds

    OFFSET = repeat((0, 0))  # idk what this does but it is for the screen shake

    def __init__(self, window: pygame.Surface, window_w, window_h, players: list[Player], gravity=0.5):
        self.window = window
        self.width = window_w
        self.height = window_h
        self.players = players

        self.MAP_LIMIT_BOTTOM = window_h + 500
        self.MAP_LIMIT_RIGHT = window_w + 500

        self.CENTER_X = window_w // 2
        self.CENTER_Y = window_h // 2

        self.GRAVITY = gravity

    @abstractmethod
    def _render_objects(self):
        pass

    def render(self):
        self.window.fill(self.WINDOW_BACKGROUND_COLOR)
        self._render_objects()

        for player in self.players:
            player.set_position(player.posx, player.posy)
            player.render()

        self.window.blit(self.window, next(self.OFFSET))

    def vertical_colision_detection(self):
        for player in self.players:
            # check is player is out of the map

            self._handle_limits(player)

            '''if player.posy >= MAP_LIMIT_BOTTOM or player.posy <= MAP_LIMIT_TOP: #Mettre cette section si dans une
             fonction appart (would be clean)
                player.set_position(700, 100)
                global OFFSET
                OFFSET = screen_shake(5, 40)

            elif player.posx >= MAP_LIMIT_RIGHT or player.posx <= MAP_LIMIT_LEFT:
                player.set_position(20, 100)
                OFFSET = screen_shake(700, 40)'''

            for block in self.BLOCKS:

                if player.posy + player.size + player.y_vel >= block.posy >= player.posy + player.size:

                    # case num.1: the block is directly on the left edge
                    if block.posx <= player.right_edge <= block.right_edge:

                        player.colision_reset(block)
                        break

                    # case num.2: player is on the right edge of the block
                    elif block.posx <= player.posx <= block.right_edge:

                        player.colision_reset(block)
                        break

                    # case num.3: if the block is smaler then the player size
                    elif player.posx <= block.posx and player.right_edge >= block.right_edge:

                        player.colision_reset(block)
                        break

                    else:
                        player.vert_colision = False

    # Return True if the player is out boundries or of the window (return false if player is visible)
    # respawn player if he touches the outside limit (and play animation) (show arrow when player is not visible)
    def _handle_limits(self, player: Player):

        if player.posy < 0 or player.posy > self.height:  # check if player is outside visible window in Y

            if player.posy >= self.MAP_LIMIT_BOTTOM or player.posy <= self.MAP_LIMIT_TOP:
                player.set_position(700, 100)
                self.OFFSET = self._screen_shake(5, 40)
            else:  # player not out but not visible (display an arrow)
                self._arrow_direction(player)
                '''pygame.draw.polygon(window, (0, 0, 0),
                                    ((0, 100), (0, 200), (200, 200), (200, 300), (300, 150), (200, 0), (200, 100)))'''

        elif player.posx < 0 or player.posx > self.width:  # check if player is outside visible window in X

            if player.posx >= self.MAP_LIMIT_RIGHT or player.posx <= self.MAP_LIMIT_LEFT:
                player.set_position(700, 100)
                self.OFFSET = self._screen_shake(5, 40)

            else:  # player not out but not visible (display an arrow)
                self._arrow_direction(player)
                '''pygame.draw.polygon(window, (0, 0, 0),
                                    ((0, 100), (0, 200), (200, 200), (200, 300), (300, 150), (200, 0), (200, 100)))'''
        else:
            return False

    def _arrow_direction(self, player: Player):
        origine = (self.CENTER_X, self.CENTER_Y)
        end_pos = (player.posx, player.posy)

        line = pygame.draw.line(self.window, (0, 0, 0), origine, end_pos, width=5)
        pygame.display.update(line)  # Update the line only

    @staticmethod
    def _screen_shake(intensity, amplitude):
        s = -1
        for i in range(0, 15):
            for x in range(0, amplitude, intensity):
                yield x * s, 0
            for x in range(amplitude, 0, intensity):
                yield x * s, 0
            s *= -1
        while True:
            yield 0, 0
