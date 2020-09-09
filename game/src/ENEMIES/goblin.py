"""
Goblin entity file
author: Joshua Akangah
date: 8/9/20
"""

from .manager import *

class Goblin(EnemyEntity):
    def __init__(self, base_state, typeOf, x, y):
        EnemyEntity.__init__(self, base_state, typeOf, x, y)
        self.speed = 1.2
        self.can_fly = False
        self.isFalling = True
        self.look_states = ['die', 'damage']
        self.is_hostile = True
        self.look_distance = 200
        self.attack_distance = 0.3

    def update(self, dt, player):
        super(Goblin, self).update(dt, player)

        if self.is_hostile:
            if self.flip:
                if self.rect.x < player.rect.x + player.rect.width + self.attack_distance:
                    self.is_attacking = True
                else:
                    self.is_attacking = False
            else:
                if self.rect.x + self.rect.width > player.rect.x - self.attack_distance:
                    self.is_attacking = True
                else:
                    self.is_attacking = False

        if self.dead:
            if self.rect.bottom < DISPLAY_SIZE[1]:
                self.isFalling = True
            else:
                self.isFalling = False

        print(self.is_taking_damage)


    def doAnimations(self, dt):
        super(Goblin, self).doAnimations(dt)

        if self.current_state in self.look_states:
            if not self.animation.is_last_image():
                self.animation.animate(dt)
            else:
                if self.dead:
                    pass
                if self.is_taking_damage:
                    self.is_taking_damage = False
        else:
            self.animation.animate(dt)


    def updateStates(self):
        super(Goblin, self).updateStates()

        entity_state = 'idle'

        if self.dead:
            entity_state = 'die'

        if self.isMoving and not self.dead:
            entity_state = 'move'

        if self.is_attacking and not self.dead:
            entity_state = 'attack'

        if self.is_taking_damage and not self.dead:
            entity_state = 'damage'

        self.setState(entity_state)
