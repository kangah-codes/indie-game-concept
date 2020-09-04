"""
Main player class module
author: Joshua Akangah
date: 10/8/20
"""

from .settings import *
from GLOBAL.physics import *
from .load_sprites import *

class Player(pygame.sprite.Sprite, PhysicsObject):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        PhysicsObject.__init__(self, 100, 0)

        self.base_state = 'idle_no_sword' # base state for player
        self.current_state = self.base_state
        self.animation = Animation(player_states.get(self.current_state), 1.0)
        self.current_frame = self.animation.get_current_image()
        self.animation_rect = self.current_frame.get_rect()

        self.image = pygame.Surface((20, self.animation_rect.height - 5))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()

        # states
        self.flip = False
        self.is_crouching = False
        self.is_running = False

    def update(self, dt):
        self.rect.x, self.rect.y = self.pos.x, self.pos.y
        self.animation.animate(dt)
        self.animation_rect = self.current_frame.get_rect()
        self.animation_rect.center = self.rect.center

        self.current_frame = self.animation.get_current_image()

        # check if player rect is leaving vertical bounds
        if self.pos.y + self.rect.height >= DISPLAY_SIZE[1] and not self.isJumping:
            self.touchingGround = True
            self.pos.y = DISPLAY_SIZE[1] - self.rect.height

        # check if player is moving
        if self.acc.x != 0:
            self.isMoving = True


        self.simulateGravity(dt)
        self.simulateMotion()
        self.handleKeypress()

        self.updateStates()

    def draw(self, display):
        self.image.fill(WHITE)
        display.blit(self.image, (self.rect.x, self.rect.y))
        display.blit(pygame.transform.flip(self.current_frame, self.flip, False), (self.animation_rect.x, self.rect.y - 5))

    def handleKeypress(self):
        keyPress = pygame.key.get_pressed()
        self.acc = pygame.math.Vector2(0, 800)

        if keyPress[pygame.K_d]:
            self.isMoving = True
            self.flip = False

        if keyPress[pygame.K_a]:
            self.isMoving = True
            self.flip = True

        if keyPress[pygame.K_a] or keyPress[pygame.K_d]:
            if self.is_crouching:
                self.acc.x = 0.1 if not self.flip else -0.1
            else:
                self.acc.x = 0.5 if not self.flip else -0.5

        if not (keyPress[pygame.K_a] or keyPress[pygame.K_d]):
            self.isMoving = False

        if keyPress[pygame.K_s]:
            self.is_crouching = True
        else:
            self.is_crouching = False

    def updateStates(self):
        print(self.isMoving)
        if self.is_crouching and self.touchingGround and not self.isMoving:
            self.setState('crouch')
        elif self.is_crouching and self.isMoving:
            self.setState('crouch_walk')

        else:
            self.setState(self.base_state)

    def setState(self, state):
        if self.current_state != state:
            self.current_state = state
            self.animation = Animation(player_states.get(self.current_state), 1.0)
