from abc import ABC
import pygame
from world.object import Block


class Player(ABC):

    GRAVITY = 1
    def __init__(self, window, spawn_x, spawn_y, size, ai_controlled=False):  # Todo add player image location
        self.posx = spawn_x
        self.posy = spawn_y
        self.x_vel = 0.8 #velocity by default for the x axis
        self.y_vel = 0.8 #velocity by default for the y axis
        self.fall_count = 0 #how much time the player has been falling for (makes it possible to calculate the future velocity/acceleration)
        self.size = size
        self.right_edge = self.posx+self.size #position of the pixel of the player thats the most to the right
        self.window = window
        self.vert_colision = False

    def render(self):
        pygame.draw.rect(self.window, (255, 0, 0), (self.posx, self.posy, self.size, self.size))
        print('hello')
    def set_position(self, posx, posy):
        self.posx = posx
        self.posy = posy
        self.right_edge = self.posx + self.size

    def move_right(self):
        self.posx += self.x_vel

    def move_left(self):
        self.posx -= self.x_vel

    def jump(self):
        self.y_vel = -1.5
        self.fall_count = 0
        self.vert_colision = False

    def move_down(self):
        self.posy += self.y_vel
        self.vert_colision = False

    def colision_reset(self, block):
        self.set_position(self.posx, block.posy - self.size)
        self.y_vel = 0
        self.fall_count = 0
        self.vert_colision = True


