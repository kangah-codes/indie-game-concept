"""
Class for parallax bg object
author: Joshua Akangah
date: 15/8/20
"""

from .backgrounds import *

class Background():
    def __init__(self, image, pos):
        self.x = pos[0]
        self.y = pos[1]
        self.image = image

    def update(self):
        if self.x < -DISPLAY_SIZE[0]:
            self.x = 0

        if self.x > DISPLAY_SIZE[0]:
            self.x = 0

        if self.x < 0:
            self.newX = DISPLAY_SIZE[0] - math.fabs(self.x)

        if self.x > 0:
            self.newX = -DISPLAY_SIZE[0] + math.fabs(self.x)

    def draw(self, display):
        if self.x < 0 or self.x > 0:
            display.blit(self.image, (self.newX, self.y))
        display.blit(self.image, (self.x, self.y))

    def move(self, x):
        self.x += x
