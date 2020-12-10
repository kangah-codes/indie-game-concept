"""
Portal entity for spawning and managing portals
author - Joshua Akangah
date - 22/10/20
"""

from .settings import *

# portal animations
portal_animations = {
    'idle': [
        os.path.join(BASE_DIR, 'assets/EFFECTS/PORTAL/20.png'),
    ],
    'open': [
        os.path.join(BASE_DIR, 'assets/EFFECTS/PORTAL/0.png'),
        os.path.join(BASE_DIR, 'assets/EFFECTS/PORTAL/3.png'),
        os.path.join(BASE_DIR, 'assets/EFFECTS/PORTAL/4.png'),
        os.path.join(BASE_DIR, 'assets/EFFECTS/PORTAL/5.png'),
        os.path.join(BASE_DIR, 'assets/EFFECTS/PORTAL/6.png'),
        # os.path.join(BASE_DIR, 'assets/EFFECTS/PORTAL/7.png'),
        os.path.join(BASE_DIR, 'assets/EFFECTS/PORTAL/8.png'),
        os.path.join(BASE_DIR, 'assets/EFFECTS/PORTAL/9.png'),
    ],
    # reverse this list to get open
    'open_close_animation': [
        os.path.join(BASE_DIR, 'assets/EFFECTS/PORTAL/19.png'),
        os.path.join(BASE_DIR, 'assets/EFFECTS/PORTAL/13.png'),
        os.path.join(BASE_DIR, 'assets/EFFECTS/PORTAL/15.png'),
        os.path.join(BASE_DIR, 'assets/EFFECTS/PORTAL/16.png'),
        os.path.join(BASE_DIR, 'assets/EFFECTS/PORTAL/18.png'),
        os.path.join(BASE_DIR, 'assets/EFFECTS/PORTAL/17.png'),
    ]
}

class Portal(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.pos = pygame.math.Vector2(x, y)
        self.to = None
        self.base_state = 'idle'
        self.current_state = self.base_state
        self.animation = Animation(portal_animations.get(self.base_state), 0.25, 0.125)
        self.image = self.animation.get_current_image()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, dt, player):
        if self.pos.y + self.rect.height < DISPLAY_SIZE[1]:
            self.pos.y += 1
        else:
            self.pos.y = DISPLAY_SIZE[1] - self.rect.height

        self.rect.x, self.rect.y = self.pos.x, self.pos.y
        self.rect = self.image.get_rect()
        print(self.rect.x, self.pos.x)
        self.rect.x, self.rect.y = self.pos.x, self.pos.y
        self.image = self.animation.get_current_image()
        self.animation.animate(dt)

        if self.current_state == 'open_close_animation':
            if self.animation.is_last_image():
                self.setState('open')

        if pygame.sprite.collide_mask(player, self):
            if self.current_state == 'idle':
                self.setState('open_close_animation', True)
            # if not self.animation.is_last_image():
            #     print('lol')
            # else:
            #     self.setState('open')
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
                    portal_animations.get(self.current_state)[::-1], 1.0, 0.125
                )
                return
            self.animation = Animation(
                portal_animations.get(self.current_state), 1.0, 0.125
            )

    def draw(self, display):
        display.blit(self.image, (self.pos.x, self.pos.y))
