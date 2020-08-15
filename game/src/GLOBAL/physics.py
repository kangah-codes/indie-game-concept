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
        self.friction = -0.12
        self.speed = 3
    
    def simulateGravity(self, dt):
        if self.isFalling or self.isJumping:
            self.pos.y += self.vel.y * (dt/FPS*2)
            self.vel.y += self.acc.y * (dt/FPS*2)
            
            if self.vel.y >= 0:
                self.isJumping = False
                self.isFalling = True

            elif self.vel.y < 0:
                self.isJumping = True
                self.isFalling = False
    
    def simulateFriction(self, dt):
        self.friction = -dt