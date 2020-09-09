"""
Bat entity file
author: Joshua Akangah
date: 7/9/20
"""

from .manager import *

class Bat(EnemyEntity):
    def __init__(self, base_state, typeOf, x, y):
        EnemyEntity.__init__(self, base_state, typeOf, x, y)
        self.speed = 0.5
        self.can_fly = True
        self.look_distance = 400

    def update(self, dt, player):
        super(Bat, self).update(dt, player)

        if self.dead:
            self.can_fly = False

    def doAnimations(self, dt):
        super(Bat, self).doAnimations(dt)

        if not self.dead:
            self.animation.animate(dt)
