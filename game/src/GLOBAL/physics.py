"""
    Player physics object
    author: Joshua Akangah
    date: 11/8/20
"""

from CONFIG.settings import *

class PhysicsObject():
    def __init__(self, x, y):
        self.isFalling = True
        self.isJumping = False
        self.isMoving = False
        self.movingDirection = 1 # default movingDirection


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

    def simulateJump(self):
        self.isJumping = True
        self.vel.y = -400

    def simulateFriction(self):
        # apply friction
        self.acc.x += self.vel.x * self.friction

        # equations of motion
        self.vel.x += self.acc.x
        self.pos.x += self.vel.x + 0.5 * self.acc.x

    def move(self, direction):
        self.isMoving = True
        self.movingDirection = direction

        if direction == 1:
            self.pos.x += self.speed
        elif direction == 0:
            self.pos.x -= self.speed
