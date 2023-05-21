from abc import ABC
import pygame


class Player(ABC):

    def __init__(self, window, spawn_x, spawn_y, ai_controlled=False):  # Todo add player image location
        self.posx = spawn_x
        self.posy = spawn_y

        self.window = window

    def render(self, ):
        pygame.draw.rect(self.window, (255, 0, 0), (self.posx, self.posy, 20, 20))
        pygame.display.update()

    def set_position(self, posx, posy):
        self.posx = posx
        self.posy = posy
