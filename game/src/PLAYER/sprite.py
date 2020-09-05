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
        self.is_running_fast = False
        self.is_walking = False
        self.is_sliding = False

        # additional
        self.can_double_jump = True
        self.is_double_jumping = False
        self.jump_count = 0

    def update(self, dt):
        self.rect.x, self.rect.y = self.pos.x, self.pos.y
        self.animation_rect = self.current_frame.get_rect()
        self.animation_rect.center = self.rect.center

        self.current_frame = self.animation.get_current_image()

        # check if player rect is leaving vertical bounds
        if self.rect.y + self.rect.height >= DISPLAY_SIZE[1] and not self.isJumping:
            self.touchingGround = True
            self.pos.y = DISPLAY_SIZE[1] - self.rect.height
            self.isFalling = False

        if self.rect.y + self.rect.height < DISPLAY_SIZE[1]:
            self.touchingGround = False

        # check if player is moving
        if self.acc.x != 0:
            self.isMoving = True

        # touching ground check
        if self.touchingGround:
            if not self.isMoving and not self.is_crouching and not self.is_sliding:
                self.setState(self.base_state)

            self.is_double_jumping = False
            self.can_double_jump = True
            self.jump_count = 0

        if self.jump_count >= 2:
            self.can_double_jump = False

            self.is_double_jumping = True

        self.simulateGravity(dt)
        self.simulateMotion()
        self.handleKeypress()
        self.doAnimations(dt)
        self.updateStates()

    def doAnimations(self, dt):
        # locking frames to last
        if self.isJumping or self.is_sliding:
            if not self.animation.is_last_image():
                self.animation.animate(dt)
            else:
                if self.is_sliding:
                    self.is_sliding = False
                    self.isMoving = False
        else:
            self.animation.animate(dt)


    def draw(self, display):
        self.image.fill(WHITE)
        display.blit(self.image, (self.rect.x, self.rect.y))
        display.blit(pygame.transform.flip(self.current_frame, self.flip, False), (self.animation_rect.x, self.rect.y - 5))

    def handleKeypress(self):
        keyPress = pygame.key.get_pressed()
        self.acc = pygame.math.Vector2(0, 800)

        if keyPress[pygame.K_d] or keyPress[pygame.K_RIGHT]:
            self.flip = False

        if keyPress[pygame.K_a] or keyPress[pygame.K_LEFT]:
            self.flip = True

        if (keyPress[pygame.K_a] or keyPress[pygame.K_d]):
            self.is_running = True

        if keyPress[pygame.K_RIGHT] or keyPress[pygame.K_LEFT]:
            self.is_walking = True

        if (keyPress[pygame.K_a] or keyPress[pygame.K_d]) or (keyPress[pygame.K_RIGHT] or keyPress[pygame.K_LEFT]):
            self.isMoving = True

            if self.is_crouching or self.is_walking:
                self.acc.x = 0.1 if not self.flip else -0.1
            else:
                self.acc.x = 0.3 if not self.flip else -0.3

        if not (keyPress[pygame.K_RIGHT] or keyPress[pygame.K_LEFT]):
            self.is_walking = False

        if not (keyPress[pygame.K_a] or keyPress[pygame.K_d] or keyPress[pygame.K_RIGHT] or keyPress[pygame.K_LEFT]):
            self.isMoving = False
            self.is_running = False

        if keyPress[pygame.K_s]or keyPress[pygame.K_DOWN]:
            self.is_crouching = True

        if not (keyPress[pygame.K_s] or keyPress[pygame.K_DOWN]):
            self.is_crouching = False


    def updateStates(self):
        """
        STATES
        self.is_crouching
        self.is_running
        self.is_running_fast
        self.is_walking
        self.is_sliding
        self.isJumping
        self.isFalling
        self.isMoving
        """
        # default
        if not self.is_sliding and not self.is_crouching\
            and not self.isMoving and not self.is_running\
            and not self.is_walking and not self.is_running_fast\
            and not (self.isFalling or self.isJumping): self.setState(self.base_state)

        # player sliding
        if self.is_sliding and not self.is_crouching\
            and not self.is_running and not self.is_walking\
            and not self.is_running_fast and \
            not (self.isFalling or self.isJumping): self.setState('slide')

        # player running
        if self.is_running and not self.is_crouching\
            and not self.is_walking and not self.is_sliding\
            and not self.is_running_fast and\
            not self.isFalling and not self.isJumping: self.setState('sprint_slow')

        # jumping
        if self.isJumping and not self.isFalling:
            if self.is_double_jumping:
                self.setState('jump_flip')
            else:
                self.setState('jump')

        # falling
        if self.isFalling and not self.isJumping: self.setState('fall')

        # crouching
        if self.is_crouching and not self.isMoving\
            and not self.is_running and not self.is_sliding\
            and not self.is_walking and not self.is_running_fast\
            and not (self.isJumping or self.isFalling): self.setState('crouch')

        # crouch walking
        if self.is_crouching and self.isMoving: self.setState('crouch_walk')

        # is_walking
        if self.is_walking and not self.isJumping\
            and not self.is_sliding and not self.is_crouching\
            and not self.is_running\
            and not self.is_running_fast: self.setState('walk')

        # crouch walk
        # if self.is_crouching and self.isMoving\
        #     and not self.is_running and not self.is_sliding\
        #     and not self.is_walking and not self.is_running_fast\
        #     and not (self.isJumping or self.isFalling):
        #     self.setState('crouch_walk')

    def setState(self, state):
        if self.current_state != state:
            self.current_state = state
            self.animation = Animation(player_states.get(self.current_state), 1.0)

    # state functions
    def slide(self):
        self.is_sliding = True
        self.is_moving = True
        self.setState('slide')
        self.acc.x = 10 if not self.flip else -10

    # simulate jumping
    def simulateJump(self):
        if self.can_double_jump:
            self.isJumping = True
            self.touchingGround = False
            self.vel.y = -400
            self.jump_count += 1
