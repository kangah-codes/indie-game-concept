"""
Bat entity file
author: Joshua Akangah
date: 7/9/20
"""

from ..manager import *

class Bat(EnemyEntity):
    def __init__(self, base_state, typeOf, x, y):
        EnemyEntity.__init__(self, base_state, typeOf, x, y)
        self.speed = 0.5

    def move_to_player(self, player):
        dx, dy = player.rect.x - self.rect.x, player.rect.y - self.rect.y
        dist = math.hypot(dx, dy)

        if dist != 0:
            dx, dy = dx / dist, dy / dist  # Normalize.
        # Move along this normalized vector towards the player at current speed.
        self.pos.x += dx * self.speed
        self.pos.y += dy * self.speed


    def update(self, dt, player):
        super(Bat, self).update(dt)

        self.move_to_player(player)
