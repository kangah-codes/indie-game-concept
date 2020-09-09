"""
Eye entity file
author: Joshua Akangah
date: 8/9/20
"""

from .manager import *

class Eye(EnemyEntity):
    def __init__(self, base_state, typeOf, x, y):
        EnemyEntity.__init__(self, base_state, typeOf, x, y)
        self.speed = 1
        self.isFalling = True
        self.look_states = ['die', 'idle', 'damage']
        self.is_hostile = True
        self.can_fly = True
        self.look_distance = 100

    def update(self, dt, player):
        super(Eye, self).update(dt, player)

        if self.dead:
            self.can_fly = False

        if abs(player.rect.x - self.rect.x) <= self.look_distance/2:
            self.is_attacking = True
        else:
            self.is_attacking = False

    def doAnimations(self, dt):
        super(Eye, self).doAnimations(dt)

        if self.current_state in self.look_states:
            if not self.animation.is_last_image():
                self.animation.animate(dt)
            else:
                if self.dead:
                    self.kill()
                if self.current_state == 'idle':
                    pass
                if self.is_taking_damage:
                    self.is_taking_damage = False
        else:
            self.animation.animate(dt)


    def updateStates(self):
        super(Eye, self).updateStates()

        entity_state = 'idle'

        if self.is_idle and not self.dead:
            entity_state = 'idle'

        if self.player_in_sight and not self.dead:
            entity_state = 'move'

        if self.dead:
            entity_state = 'die'

        if self.is_attacking and not self.dead:
            entity_state = 'attack'

        if self.is_taking_damage and not self.dead:
            entity_state = 'damage'


        self.setState(entity_state)

    def fly_to_player(self, player):
        self.dx, self.dy = player.rect.x - self.rect.x, player.rect.centery - self.rect.y
        dist = math.hypot(self.dx, self.dy)

        if dist != 0:
            self.dx, self.dy = self.dx / dist, self.dy / dist  # Normalize.

        if abs(player.rect.x - self.rect.x) > self.look_distance/2:
            self.pos.x += self.dx * self.speed

        self.pos.y += self.dy * self.speed
