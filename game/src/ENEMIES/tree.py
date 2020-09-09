"""
Tree entity file
author: Joshua Akangah
date: 8/9/20
"""

from .manager import *

class Tree(EnemyEntity):
    def __init__(self, base_state, typeOf, x, y):
        EnemyEntity.__init__(self, base_state, typeOf, x, y)
        self.speed = 0.5
        self.can_fly = False
        self.isFalling = True
        self.look_states = ['die']
        self.is_hostile = True

    def update(self, dt, player):
        super(Tree, self).update(dt, player)

        if self.is_hostile:
            if abs(self.dx) <= 0.1:
                self.is_attacking = True
            else:
                self.is_attacking = False

    def doAnimations(self, dt):
        super(Tree, self).doAnimations(dt)

        if self.current_state in self.look_states:
            if not self.animation.is_last_image():
                self.animation.animate(dt)
            else:
                if self.dead:
                    pass
        else:
            self.animation.animate(dt)


    def updateStates(self):
        super(Tree, self).updateStates()

        entity_state = 'idle'

        if not self.isMoving and not self.dead:
            entity_state = 'idle'

        if self.isMoving and self.touchingGround and not self.dead:
            entity_state = 'move'

        if self.is_attacking and not self.dead:
            entity_state = 'attack'

        if self.dead:
            entity_state = 'die'

        self.setState(entity_state)

    def die(self):
        self.dead = True
