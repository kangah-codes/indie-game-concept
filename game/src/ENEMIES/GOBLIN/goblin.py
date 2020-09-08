"""
Goblin entity file
author: Joshua Akangah
date: 8/9/20
"""

from ..manager import *

class Goblin(EnemyEntity):
    def __init__(self, base_state, typeOf, x, y):
        EnemyEntity.__init__(self, base_state, typeOf, x, y)
        self.speed = 1.2
        self.can_fly = False
        self.isFalling = True
        self.look_states = ['die', 'damage']
        self.is_hostile = True
        self.look_distance = 200

    def update(self, dt, player):
        super(Goblin, self).update(dt, player)

        if self.is_hostile:
            if abs(self.dx) <= 0.1:
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

    def move_to_player(self, player):
        self.dx, self.dy = player.rect.x - self.rect.x, player.rect.centery - self.rect.y
        dist = math.hypot(self.dx, self.dy)

        if dist != 0:
            self.dx /= dist  # Normalize.
        # Move along this normalized vector towards the player at current speed.
        # self.pos.x += self.dx * self.speed

        if abs(player.rect.x - self.rect.x) > 50:
            self.pos.x += self.dx * self.speed
        #self.pos.x += self.dx * self.speed
