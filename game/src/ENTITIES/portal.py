"""
Portal entity for spawning and managing portals
author - Joshua Akangah
date - 22/10/20
"""

from .settings import *

green_spritesheet = Spritesheet(os.path.join(BASE_DIR, 'assets/EFFECTS/PORTAL/green.png'))
purple_spritesheet = Spritesheet(os.path.join(BASE_DIR, 'assets/EFFECTS/PORTAL/purple.png'))

# portal animations
portal_animations = {
    'open_idle_green': green_spritesheet.images_at((
        (25,15,13,42),
        (89,16,13,41),
        (281,15,13,42),
        (89,16,13,41),
        (217,16,13,41),
        (345,16,13,41),
        (472,16,14,41),
    ), colorkey=WHITE),
    'open_green': green_spritesheet.images_at((
        (19,95,23,1),
        (81,95,27,3),
        (145,93,27,8),
        (214,90,17,17),
        (281,81,13,34),
        (345,78,13,43),
        (409,81,13,40),
        (473,79,13,42),
    ), colorkey=WHITE),
    'close_green': green_spritesheet.images_at((
        (25, 145, 13, 34),
        (86,154,17,17),
        (145,157,27,8),
        (209,159,27,3),
        (268,159,7,1),
    ), colorkey=WHITE),
    'open_idle_purple': purple_spritesheet.images_at((
        (25,15,13,42),
        (89,16,13,41),
        (281,15,13,42),
        (89,16,13,41),
        (217,16,13,41),
        (345,16,13,41),
        (472,16,14,41),
    ), colorkey=(255,255,255)),
    'open_purple': purple_spritesheet.images_at((
        (19,95,23,1),
        (81,95,27,3),
        (145,93,27,8),
        (214,90,17,17),
        (281,81,13,34),
        (345,78,13,43),
        (409,81,13,40),
        (473,79,13,42),
    ), colorkey=WHITE),
    'close_purple': purple_spritesheet.images_at((
        (25, 145, 13, 34),
        (86,154,17,17),
        (145,157,27,8),
        (209,159,27,3),
        (268,159,7,1),
    ), colorkey=WHITE),
}

class Portal(pygame.sprite.Sprite):
    def __init__(self, x, y, typeOf):
        pygame.sprite.Sprite.__init__(self)
        self.pos = pygame.math.Vector2(x, y)
        self.to = None
        self.type = typeOf
        self.base_state = 'open_idle'
        if self.type == 0:
            self.base_state += '_green'
        else:
            self.base_state += '_purple'
        self.sprites = portal_animations.get(self.base_state)
        self.current_state = self.base_state
        self.animation = Animation(self.sprites, 0.9, 0.125, use_surface=True)
        self.image = self.animation.get_current_image()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.player_entered = False
        self.player_exited = False
        self.player = None
        self.blit = True
        self.center = None

    def update_portal(self, dt, player):
        self.player = player if self.player is None else player
        self.to.blit = False if self.to.player_exited == False else True

        # if self.pos.y + self.rect.height < DISPLAY_SIZE[1]:
        #     self.pos.y += 1
        # else:
        #     self.pos.y = DISPLAY_SIZE[1] - self.rect.height

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.pos.x, self.pos.y
        self.image = self.animation.get_current_image()
        self.mask = pygame.mask.from_surface(self.image)
        self.animation.animate(dt)

        if pygame.sprite.collide_mask(player, self) and self.blit:
            if player.rect.centerx < self.rect.centerx: # player is to the left
                if player.rect.right >= self.rect.left:
                    player.pos.x = self.to.rect.right
            elif player.rect.centerx > self.rect.centerx: # player is to the right
                if player.rect.left <= self.rect.right:
                    player.pos.x = self.to.rect.left - player.rect.width
            self.to.player_exited = True
            self.player_entered = True

        self.updateStates()

    def update(self, dt, player):
        if self.blit:
            self.update_portal(dt, player)

    def updateStates(self):
        if not self.player_exited and not self.player_entered:
            state = self.base_state
            self.center = [self.rect.centerx, self.rect.centery]
            # print(self.center)
        else:
            if self.player_exited:
                state = ['open_' + 'green' if self.type == 0 else 'open_' + 'purple'][0]
            if self.player_entered:
                state = ['close_' + 'green' if self.type == 0 else 'close_' + 'purple'][0]


        if self.player_entered:
            if self.animation.is_last_image():
                self.player_entered = False
                self.blit = False

        if self.player_exited:
            # self.pos.x, self.pos.y = self.center[0], self.center[1]
            if self.animation.is_last_image():
                self.player_exited = False
                self.blit = True

        self.setState(state)


    def setState(self, state, reverse=False):
        if self.current_state != state:
            self.current_state = state
            if reverse:
                self.animation = Animation(
                    portal_animations.get(self.current_state)[::-1], 1.0, 0.125, True
                )
                return
            if 'close' in self.current_state:
                self.animation = Animation(portal_animations.get(self.current_state), 1.0, 0.1, True)
                return
            self.animation = Animation(
                portal_animations.get(self.current_state), 1.0, 0.125, True
            )

    def draw(self, display):
        if self.blit:
            display.blit(self.image, (self.pos.x, self.pos.y))
