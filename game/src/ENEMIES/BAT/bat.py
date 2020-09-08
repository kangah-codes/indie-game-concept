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
        self.can_fly = True

    def update(self, dt, player):
        super(Bat, self).update(dt, player)

        # self.move_to_player(player)

    def doAnimations(self, dt):
        super(Bat, self).doAnimations()

        self.animation.animate(dt)

    def die(self):
        if self.rect.bottom < DISPLAY_SIZE[1]:
            self.simulateGravity()
        else:
            self.dead = True
