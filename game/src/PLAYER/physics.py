"""
    Player physics object
    author: Joshua Akangah
    date: 11/8/20
"""

from CONFIG.settings import *

class PhysicsObject():
    def __init__(self, x, y):
        self.accelX, self.accelY = 0, 800
        self.velX, self.velY = 0, 0
        self.isFalling = True
        self.isJumping = False
        self.pos = pygame.math.Vector2(x, y)
        self.acc = pygame.math.Vector2(0, 800)
        self.vel = pygame.math.Vector2(0, 0)
    
    def simulateGravity(self):
        if self.isFalling or self.isJumping:
            self.pos.y += self.vel.y * (30/1000.0)
            self.vel.y += self.acc.y * (30/1000.0)
            
            if self.vel.y >= 0:
                self.isJumping = False
                self.isFalling = True

            elif self.vel.y < 0:
                self.isJumping = True
                self.isFalling = False