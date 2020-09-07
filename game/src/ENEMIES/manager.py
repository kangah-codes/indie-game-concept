"""
Enemy entity manager
author: Joshua Akangah
date: 7/9/20
"""

from .settings import *
from .load_sprites import *
from GLOBAL.physics import *
from GLOBAL.animation import *

class EnemyEntity(PhysicsObject, pygame.sprite.Sprite):
    def __init__(self, base_state, typeOf, x, y):
        PhysicsObject.__init__(self, x, y)
        pygame.sprite.Sprite.__init__(self)

        self.base_state = base_state
        self.current_state = self.base_state
        self.type = typeOf
        self.dict_object = enemy_animations.get(self.type)

        self.animation = Animation(self.dict_object.get(self.base_state), self.dict_object.get('scale'))
        self.current_frame = self.animation.get_current_image()
        self.rect = self.current_frame.get_rect()
        self.mask = pygame.mask.from_surface(self.current_frame)
        self.image = self.current_frame

        self.health = self.dict_object.get('health')
        self.dead = False

    def update(self, dt):
        self.doAnimations(dt)

        self.rect.x, self.rect.y = self.pos.x, self.pos.y

    def doAnimations(self, dt):
        self.animation.animate(dt)

        self.current_frame = self.animation.get_current_image()
        self.rect = self.current_frame.get_rect()
        self.mask = pygame.mask.from_surface(self.current_frame)
        self.image = self.current_frame

    def draw(self, display):
        pygame.draw.rect(display, BLUE, ((self.pos.x+self.rect.width/2)-(self.health*10/2), self.pos.y - 5, self.health*10, 2))
        display.blit(self.current_frame, (self.pos.x, self.pos.y))

    def updateStates(self):
        pass

    def die(self):
        if self.pos.y + self.rect.height < DISPLAY_SIZE[1]:
            self.simulateGravity()
        else:
            self.dead = True
