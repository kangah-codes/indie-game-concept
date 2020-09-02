"""
Main player class module
author: Joshua Akangah
date: 10/8/20
"""

from .settings import *
from GLOBAL.physics import *

class Player(pygame.sprite.Sprite, PhysicsObject):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        PhysicsObject.__init__(self, 100, 0)
        self.animation = None
        self.image = pygame.Surface((50, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()

    def update(self, dt):
        self.rect.x, self.rect.x = self.pos.x, self.pos.y

        if self.pos.y + self.rect.height < DISPLAY_SIZE[1]:
            self.simulateGravity(dt)

    def draw(self, display):
        display.blit(self.image, self.pos)
