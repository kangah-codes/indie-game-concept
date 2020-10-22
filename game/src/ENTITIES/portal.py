"""
Portal entity for spawning and managing portals
author - Joshua Akangah
date - 22/10/20
"""

from .settings import *

# portal animations
portal_animations = {
    'idle': [
        os.path.join(BASE_DIR, 'assets/EFFECTS/PORTAL/0.png'),
        os.path.join(BASE_DIR, 'assets/EFFECTS/PORTAL/3.png'),
        os.path.join(BASE_DIR, 'assets/EFFECTS/PORTAL/4.png'),
        os.path.join(BASE_DIR, 'assets/EFFECTS/PORTAL/5.png'),
        os.path.join(BASE_DIR, 'assets/EFFECTS/PORTAL/6.png'),
        os.path.join(BASE_DIR, 'assets/EFFECTS/PORTAL/7.png'),
        os.path.join(BASE_DIR, 'assets/EFFECTS/PORTAL/8.png'),
        os.path.join(BASE_DIR, 'assets/EFFECTS/PORTAL/9.png'),
    ]
}

class Portal(pygame.sprite.Sprite):
    def __init__(self, x, y, from_biome, to_biome):
        pygame.sprite.Sprite.__init__(self)
        self.pos = pygame.math.Vector2(x, y)
        self.from_biome = from_biome
        self.to_biome = to_biome
        self.base_state = 'idle'
        self.state = self.base_state
        self.animation = Animation(portal_animations.get('idle'), 1.0, 0.125)
        self.image = self.animation.get_current_image()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, dt):
        for i in self.groups():
            for sprite in i.sprites():
                print(sprite.pos.x)
        if self.pos.y + self.rect.height < DISPLAY_SIZE[1]:
            self.pos.y += 1
        else:
            self.pos.y = DISPLAY_SIZE[1] - self.rect.height

        self.rect.x, self.rect.y = self.pos.x, self.pos.y
        self.image = self.animation.get_current_image()
        self.animation.animate(dt)

class PortalChain:
    def __init__(self, portal_1, portal_2):
        self.portals = [portal_1, portal_2]

    def update(self):
        pass

    def transfer_player(self, player):
        player.pos.x, player.pos.y = portal_2.pos.x, portal_2.pos.y
