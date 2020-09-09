"""
Enemy entity manager
author: Joshua Akangah
date: 7/9/20
"""

from .settings import *
from .load_sprites import *
from GLOBAL.physics import *
from GLOBAL.animation import *
from GLOBAL.functions import *

# group for ENEMIES
class EnemyGroup(pygame.sprite.Group):
    def draw(self, surface):
        sprites = self.sprites()
        for spr in sprites:
            self.spritedict[spr] = surface.blit(spr.image, spr.rect)

            #pygame.draw.rect(surface, RED, (spr.rect.x+spr.rect.width/2-spr.health*10/spr.rect.width, spr.rect.y - 5, spr.health*10/spr.rect.width, 2))
            if spr.health > 0:
                pygame.draw.rect(surface, RED, (spr.rect.centerx-(spr.health)/2, spr.rect.y - 5, spr.health, 2))
        self.lostsprites = []

class EnemyEntity(PhysicsObject, pygame.sprite.Sprite):
    def __init__(self, base_state, typeOf, x, y):
        PhysicsObject.__init__(self, x, y)
        pygame.sprite.Sprite.__init__(self)

        self.base_state = base_state
        self.current_state = self.base_state
        self.type = typeOf
        self.dict_object = enemy_animations.get(self.type)
        self.scale = self.dict_object.get('scale')

        self.animation = Animation(self.dict_object.get(self.base_state), self.scale)
        self.image = self.animation.get_current_image()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

        self.health = self.dict_object.get('health')
        self.damage = self.dict_object.get('damage')
        self.dead = False
        self.flip = False

        self.player_in_sight = False
        self.player_in_attack_range = False
        self.is_hostile = True
        self.is_attacking = False
        self.is_idle = False if self.player_in_sight else True
        self.is_taking_damage = False
        # self.damage_on_collision = True # damage player when it collides

        # distance from player
        self.dx = None
        self.dy = None
        self.look_distance = 100

    def update(self, dt, player):
        self.doAnimations(dt)

        # changing image if flip
        if self.flip:
            if self.type == 'slime':
                self.image = pygame.transform.flip(self.image, not self.flip, False)
            else:
                self.image = pygame.transform.flip(self.image, self.flip, False)
        else:
            if self.type == 'slime':
                self.image = pygame.transform.flip(self.image, not self.flip, False)

        self.rect.x, self.rect.y = self.pos.x, self.pos.y

        if not self.dead:
            if self.is_hostile:
                self.lookForPlayer(player)

            if self.rect.x + self.rect.width < player.rect.x:
                self.flip = False
            elif self.rect.x > player.rect.x + player.rect.width:
                self.flip = True

        if not self.can_fly:
            self.simulateGravity(dt)

        # make sure entity doesnt fall over
        if self.rect.bottom >= DISPLAY_SIZE[1]:
            self.rect.y = DISPLAY_SIZE[1] - self.rect.height
            self.isFalling = False
            self.touchingGround = True

        if self.rect.bottom < DISPLAY_SIZE[1]:
            self.touchingGround = False


        if self.health <= 0:
            self.dead = True

    def doAnimations(self, dt):
        self.image = self.animation.get_current_image()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

        self.updateStates()

    def draw(self, display):
        pygame.draw.rect(display, BLUE, ((self.pos.x+self.rect.width/2)-(self.health*10/2), self.pos.y - 5, self.health*10, 2))
        display.blit(self.image, (self.rect.x, self.rect.y))

    def updateStates(self):
        pass

    def setState(self, state):
        if self.current_state != state:
            self.current_state = state
            self.animation = Animation(self.dict_object.get(self.current_state), self.scale)

    def fly_to_player(self, player):
        self.dx, self.dy = player.rect.x - self.rect.x, player.rect.centery - self.rect.y
        dist = math.hypot(self.dx, self.dy)

        if dist != 0:
            self.dx, self.dy = self.dx / dist, self.dy / dist  # Normalize.
        # Move along this normalized vector towards the player at current speed.
        self.pos.x += self.dx * self.speed
        self.pos.y += self.dy * self.speed


    def move_to_player(self, player):
        # self.dx, self.dy = player.rect.x - self.rect.x, player.rect.centery - self.rect.y
        # dist = math.hypot(self.dx, self.dy)
        #
        # if dist != 0:
        #     self.dx /= dist  # Normalize.
        # # Move along this normalized vector towards the player at current speed.
        # # self.pos.x += self.dx * self.speed
        # self.pos.x += self.dx * self.speed

        self.dx, self.dy = player.rect.x - self.rect.x, player.rect.centery - self.rect.y
        dist = math.hypot(self.dx, self.dy)
        self.dx /= dist  # Normalize.

        if self.flip:
            if self.rect.x > player.rect.x + player.rect.width:
                self.pos.x += self.dx * self.speed
        else:
            if self.rect.x + self.rect.width < player.rect.x:
                self.pos.x += self.dx * self.speed


    def lookForPlayer(self, player):
        self.is_idle = False if self.player_in_sight else True

        if abs(player.rect.x - self.rect.x) <= self.look_distance:
            if self.can_fly:
                self.fly_to_player(player)
            else:
                self.move_to_player(player)
            self.player_in_sight = True
            self.isMoving = True
        else:
            self.isMoving = False
            self.player_in_sight = False
            self.move_random()

    def move_random(self):
        pass

    def performAction(self):
        pass

    def die(self):
        pass
