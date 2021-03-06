"""
Main player class module
author:
Joshua Akangah
date:
10/8/20
"""

from .settings import *
from GLOBAL.physics import *
from .load_sprites import *


class Player(pygame.sprite.Sprite, PhysicsObject):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        PhysicsObject.__init__(self, 100, 0)

        self.base_state = 'idle_no_sword'  # base state for player
        self.current_state = self.base_state
        self.animation = Animation(player_states.get(self.current_state), 1.0)
        self.image = self.animation.get_current_image()
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.pos.x, self.pos.y

        # self.image = pygame.Surface((20, self.animation_rect.height - 5))
        # self.image.fill(WHITE)
        self.mask = pygame.mask.from_surface(self.image)

        # states
        self.flip = False
        self.is_crouching = False
        self.is_running = False
        self.is_running_fast = False
        self.is_walking = False
        self.is_sliding = False
        self.is_holding_sword = False
        self.is_drawing_sword = False
        self.is_sheathing_sword = False
        self.is_attacking = False
        self.cast_spell = False
        self.is_casting_spell = False
        self.shoot_bow = False
        self.is_shooting_bow = False
        self.is_releasing_bow = False
        self.knock_down = False
        self.is_knocked_down = False
        self.get_up = False
        self.is_getting_up = False
        self.is_punching = False

        # additional
        self.can_double_jump = True
        self.is_double_jumping = False
        self.jump_count = 0
        self.attack_level = 1
        self.punch_levels = PUNCH_LEVELS
        self.punch_level = random.choice(self.punch_levels)
        self.energy_level = ENERGY_LEVEL
        self.damage_level = 0
        self.health = 100

        # states to freeze animations with
        self.look_states = [
            'jump',
            'slide',
            'draw_sword',
            'put_back',
            'sword_attack_1',
            'sword_attack_2',
            'sword_attack_3',
            'cast_spell',
            'cast_spell_loop',
            'shoot_bow_standing',
            'release_bow',
            'release_bow_jumping',
            'stretch_bow_jumping',
            'knock_down',
            'get_up',
            'punch_1',
            'punch_2',
            'punch_3',
            'kick'
        ]

        # states to not allow movement in
        self.do_not_move = [
            'draw_sword',
            'put_back',
            'sword_attack_1',
            'sword_attack_2',
            'sword_attack_3',
            'cast_spell',
            'cast_spell_loop',
            'release_bow',
            'release_bow_jumping',
            'shoot_bow_standing',
            'hold_bow',
            'knock_down',
            'get_up',
            'punch_1',
            'punch_2',
            'kick'
        ]

        self.cast_spell_press = False
        self.shoot_bow_press = False

        self.walk_acc = 0.1
        self.run_acc = 0.3
        self.dt = 0

    def update(self, dt):
        self.mask = pygame.mask.from_surface(self.image)
        self.dt = dt
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.pos.x, self.pos.y

        self.image = self.animation.get_current_image()

        # changinf image if flip
        if self.flip:
            self.image = pygame.transform.flip(self.image, self.flip, False)

        if self.rect.bottom >= DISPLAY_SIZE[1] and not self.isJumping:
            self.touchingGround = True
            self.isFalling = False
            self.pos.y = DISPLAY_SIZE[1] - self.rect.height

        if self.rect.bottom < DISPLAY_SIZE[1]:
            self.touchingGround = False

            if not self.isJumping and not self.isFalling:
                self.pos.y = DISPLAY_SIZE[1] - self.rect.height

        # check if player is moving
        if self.acc.x != 0:
            self.isMoving = True

        # touching ground check
        if self.touchingGround:
            self.is_double_jumping = False
            self.can_double_jump = True
            self.jump_count = 0

        if self.jump_count >= 2:
            self.can_double_jump = False

            self.is_double_jumping = True

        if self.is_sliding and not self.is_knocked_down:
            self.acc.x = 0.3 if not self.flip else -0.3

        if self.energy_level >= 100:
            self.energy_level = 100

            # getting up after recharging
            if self.current_state in ['knock_down']:
                self.knock_down = False
                self.is_knocked_down = False
                self.is_getting_up = True

            if self.current_state in ['get_up']:
                if self.animation.is_last_image():
                    self.is_getting_up = False

        elif self.energy_level <= 0:
            self.energy_level = 0

        # increase energy only when resting
        if self.current_state in [self.base_state, 'idle_sword', 'knock_down']:
            self.energy_level += 0.1

        # stop shooting bow if key is released
        if not self.shoot_bow_press:
            if self.is_shooting_bow and self.animation.is_last_image():
                self.is_shooting_bow = False
                self.is_releasing_bow = True

        self.simulateGravity(dt)
        self.simulateMotion()
        self.handleKeypress()
        self.doAnimations(dt)
        self.updateStates()

    def doAnimations(self, dt):
        # locking frames to last

        if self.current_state in self.look_states:
            if not self.animation.is_last_image():
                if self.is_attacking:
                    self.animation.animate(dt*3)
                elif self.is_punching:
                    self.is_attacking = True
                    self.animation.animate(dt*2)
                else:
                    self.animation.animate(dt)
            else:
                if self.is_sliding:
                    self.is_sliding = False
                    self.isMoving = False
                if self.is_drawing_sword:
                    self.is_holding_sword = True
                    self.is_drawing_sword = False
                if self.is_sheathing_sword:
                    self.is_holding_sword = False
                    self.is_sheathing_sword = False
                if self.is_attacking:
                    self.is_attacking = False
                if self.is_punching:
                    self.is_attacking = False
                    self.is_punching = False
                if self.cast_spell:
                    self.cast_spell = False
                    self.is_casting_spell = True
                if self.is_casting_spell:
                    if self.cast_spell_press and self.energy_level > 2:
                        self.animation.animate(dt)
                    else:
                        self.is_casting_spell = False
                if self.shoot_bow:
                    self.shoot_bow = False
                    self.is_shooting_bow = True
                if self.is_shooting_bow:
                    if not self.shoot_bow_press:
                        self.is_shooting_bow = False
                        self.is_releasing_bow = True
                if self.is_releasing_bow:
                    self.is_releasing_bow = False
                if self.knock_down:
                    self.is_knocked_down = True
                    if self.is_getting_up:
                        self.is_getting_up = False
        else:
            # flipping
            if self.is_double_jumping:
                self.animation.animate(dt*3)
            else:
                self.animation.animate(dt)

    def draw(self, display):
        display.blit(self.image, (self.pos.x, self.pos.y))

    def handleKeypress(self):
        keyPress = pygame.key.get_pressed()
        self.acc = pygame.math.Vector2(0, 800)

        if keyPress[pygame.K_d] or keyPress[pygame.K_RIGHT]:
            if self.current_state not in ['knock_down']:
                self.flip = False

        if keyPress[pygame.K_a] or keyPress[pygame.K_LEFT]:
            if self.current_state not in ['knock_down']:
                self.flip = True

        if (keyPress[pygame.K_a] or keyPress[pygame.K_d]):
            self.is_running = True

        if keyPress[pygame.K_RIGHT] or keyPress[pygame.K_LEFT]:
            self.is_walking = True

        if (keyPress[pygame.K_a] or keyPress[pygame.K_d]) or (keyPress[pygame.K_RIGHT] or keyPress[pygame.K_LEFT]):
            if self.is_crouching or self.is_walking:
                if not self.current_state in self.do_not_move:
                    self.acc.x = self.walk_acc*self.dt if not self.flip else -self.walk_acc*self.dt
            else:
                if not self.current_state in self.do_not_move:
                    self.acc.x = self.run_acc*self.dt if not self.flip else -self.run_acc*self.dt

        if not (keyPress[pygame.K_RIGHT] or keyPress[pygame.K_LEFT]):
            self.is_walking = False

        if not (keyPress[pygame.K_a] or keyPress[pygame.K_d] or keyPress[pygame.K_RIGHT] or keyPress[pygame.K_LEFT]):
            self.isMoving = False
            self.is_running = False

        if keyPress[pygame.K_s] or keyPress[pygame.K_DOWN]:
            self.is_crouching = True

        else:
            self.is_crouching = False

        # handle attack 3 combo
        if keyPress[pygame.K_g] and keyPress[pygame.K_h]:
            if self.energy_level > 50 and self.is_holding_sword:  # only do when player is holding sword
                self.attack(3)
                self.energy_level -= 10

        if keyPress[pygame.K_j] and self.energy_level > ENERGY_LEVEL / 2:
            self.cast_spell_press = True
            if self.is_casting_spell:
                self.energy_level -= 2
        else:
            self.cast_spell_press = False

        if keyPress[pygame.K_b]:
            self.shoot_bow_press = True
        else:
            self.shoot_bow_press = False

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

        player_state = self.base_state if not self.is_holding_sword else 'idle_sword'

        if self.current_state == player_state: ## bug fix
            if self.is_sliding:
                self.is_sliding = False

        if self.is_running:
            if self.is_holding_sword:
                player_state = 'sprint_sword'
            else:
                player_state = 'sprint_slow'

            # edge case
            if self.is_sheathing_sword:
                player_state = 'put_back'

        if self.is_running_fast:
            if self.is_holding_sword:
                player_state = 'sprint_sword'
            else:
                player_state = 'sprint_fast'

            # edge case
            if self.is_sheathing_sword:
                player_state = 'put_back'

        if self.isJumping and not (self.shoot_bow or self.is_shooting_bow or self.is_punching):
            player_state = 'jump'

        if self.is_double_jumping:
            player_state = 'jump_flip'

        if self.isFalling and not (self.shoot_bow or self.is_shooting_bow or self.is_punching):
            if self.is_double_jumping:
                player_state = 'jump_flip'
            else:
                player_state = 'fall'

        if self.is_crouching:
            if self.isMoving:
                player_state = 'crouch_walk'
            else:
                player_state = 'crouch'

        if self.is_walking and not self.isJumping and not self.isFalling:
            player_state = 'walk'

        if self.is_sliding:
            player_state = 'slide'

        if self.is_drawing_sword and not (self.isJumping or self.isFalling or self.is_crouching):
            player_state = 'draw_sword'

        if self.is_holding_sword and not self.isMoving and not (self.isJumping or self.isFalling or self.is_crouching):
            player_state = 'idle_sword'

        if self.is_sheathing_sword and not self.isMoving and not (self.isJumping or self.isFalling or self.is_crouching):
            player_state = 'put_back'

        if self.is_attacking:
            if not self.is_punching:
                if self.attack_level == 1:
                    self.damage_level = 1
                    player_state = 'sword_attack_1'
                elif self.attack_level == 2:
                    self.damage_level = 1.5
                    player_state = 'sword_attack_2'
                else:
                    self.energy_level -= 1
                    self.damage_level = 2
                    player_state = 'sword_attack_3'

        if self.is_punching:
            if self.is_running:
                self.damage_level = 0.7
                player_state = 'punch_3'
            else:
                if self.punch_level == 1:
                    player_state = 'punch_1'
                elif self.punch_level == 2:
                    player_state = 'punch_2'
                else:
                    player_state = 'kick'
                self.damage_level = 0.5

        if not self.is_attacking:
            self.damage_level = 0

        if self.cast_spell:
            player_state = 'cast_spell'

        if self.is_casting_spell:
            player_state = 'cast_spell_loop'

        if self.shoot_bow:
            if self.isJumping or self.isFalling:
                player_state = 'stretch_bow_jumping'
            else:
                player_state = 'shoot_bow_standing'

        if self.is_shooting_bow:
            if self.isFalling or self.isJumping:
                player_state = 'hold_bow_jumping'
            else:
                player_state = 'hold_bow'

        if self.is_releasing_bow:
            if self.isFalling or self.isJumping:
                player_state = 'release_bow_jumping'
            else:
                player_state = 'release_bow'

        if self.knock_down:
            player_state = 'knock_down'

        if self.is_getting_up:
            player_state = 'get_up'

        self.setState(player_state)

        # print(self.current_state, self.is_drawing_sword)
        # print(self.is_drawing_sword, self.is_holding_sword, self.is_sheathing_sword)
        # print(self.cast_spell_press)
        # print(self.is_sliding, self.current_state)

    def setState(self, state):
        if self.current_state != state:
            self.current_state = state
            self.animation = Animation(
                player_states.get(self.current_state), 1.0)

    # state functions
    def slide(self):
        self.is_sliding = True
        self.is_moving = True
        self.setState('slide')

    # simulate jumping
    def simulateJump(self):
        if self.can_double_jump and self.current_state not in ['knock_down']:
            self.isJumping = True
            self.touchingGround = False
            self.vel.y = -400
            self.jump_count += 1

    def toggleSword(self):
        if not self.is_holding_sword:
            self.is_drawing_sword = True
            self.is_sheathing_sword = False
        else:
            self.is_sheathing_sword = True
            self.is_drawing_sword = False

    def attack(self, attackType=1):
        if self.is_attacking:
            self.animation.reset_animation()
        if self.is_holding_sword:
            self.attack_level = attackType
            self.is_attacking = True

    def castSpell(self):
        if self.energy_level > 2:
            self.cast_spell = True

    def shootBow(self):
        self.shoot_bow = True

    def knockDown(self):
        self.knock_down = True
        self.energy_level -= 50

    def getUp(self):
        self.is_getting_up = True

    def punch(self, kick=False):
        if self.is_attacking:
            self.animation.reset_animation()
        if not self.is_holding_sword or self.is_drawing_sword or self.is_sheathing_sword:
            self.punch_level = random.choice(
                self.punch_levels) if not kick else 3
            self.is_punching = True
