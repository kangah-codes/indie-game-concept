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
    'open_green': green_spritesheet.images_at((
        (25,15,13,42),
        (89,16,13,41),
        (281,15,13,42),
        (89,16,13,41),
        (217,16,13,41),
        (345,16,13,41),
        (472,16,14,41),
    ), colorkey=(255,255,255)),
    'open_purple': purple_spritesheet.images_at((
        (25,15,13,42),
        (89,16,13,41),
        (281,15,13,42),
        (89,16,13,41),
        (217,16,13,41),
        (345,16,13,41),
        (472,16,14,41),
    ), colorkey=(255,255,255)),
}

class Portal(pygame.sprite.Sprite):
    def __init__(self, x, y, typeOf):
        pygame.sprite.Sprite.__init__(self)
        self.pos = pygame.math.Vector2(x, y)
        self.to = None
        self.type = typeOf
        if self.type == 0:
            self.base_state = 'open_green'
            self.sprites = portal_animations.get(self.base_state)
            self.current_state = self.base_state
        else:
            self.base_state = 'open_purple'
            self.sprites = portal_animations.get(self.base_state)
            self.current_state = self.base_state
        self.animation = Animation(self.sprites, 0.9, 0.125, use_surface=True)
        self.image = self.animation.get_current_image()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, dt, player):
        if self.pos.y + self.rect.height < DISPLAY_SIZE[1]:
            self.pos.y += 1
        else:
            self.pos.y = DISPLAY_SIZE[1] - self.rect.height

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.pos.x, self.pos.y
        self.image = self.animation.get_current_image()
        self.mask = pygame.mask.from_surface(self.image)
        self.animation.animate(dt)

        if pygame.sprite.collide_mask(player, self):

            if player.rect.centerx < self.rect.centerx: # player is to the left
                if player.rect.right >= self.rect.left:
                    player.pos.x = self.to.rect.right
            elif player.rect.centerx > self.rect.centerx: # player is to the right
                if player.rect.left <= self.rect.right:
                    player.pos.x = self.to.rect.left - player.rect.width

    def setState(self, state, reverse=False):
        if self.current_state != state:
            self.current_state = state
            if reverse:
                self.animation = Animation(
                    portal_animations.get(self.current_state)[::-1], 1.0, 0.125, True
                )
                return
            self.animation = Animation(
                portal_animations.get(self.current_state), 1.0, 0.125, True
            )

    def draw(self, display):
        display.blit(self.image, (self.pos.x, self.pos.y))
