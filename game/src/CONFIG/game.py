"""	
Game object for handling gameplay
author: Joshua Akangah
date: 10/8/20
"""

from .settings import *
from GLOBAL.map import *


class Game:
    def __init__(self):
        self.running = True
        self.clock = CLOCK
        self.screen = pygame.display.set_mode((window_width, window_height))
        self.spriteGroup = pygame.sprite.Group()
        self.player = None
        self.background = None
        self.font = pygame.font.SysFont('Arial', 16)

        self.time_epoch = time.time()
        self.dt = time.time() - self.time_epoch

    def renderFont(self, fps):
        return self.font.render(str(round(fps)), 0, GREEN)

    def run(self):
        while self.running:
            self.dt = time.time() - self.time_epoch

            self.dt *= FPS

            self.time_epoch = time.time()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a and not self.player.usingBow:
                        self.player.isMoving = True
                        self.player.movingDirection = 0
                        self.player.isStretchingBow = False
                        self.player.usingBow = False
                    if event.key == pygame.K_d and not self.player.usingBow:
                        self.player.isMoving = True
                        self.player.movingDirection = 1
                        self.player.isStretchingBow = False
                        self.player.usingBow = False
                    if event.key == pygame.K_s:
                        self.player.isCrouching = True
                        self.isMoving = False
                        self.isCrouching = True
                        self.isStretchingBow = False
                        self.usingBow = False
                    if event.key == pygame.K_SPACE:
                        self.player.perform_jump()
                    if event.key == pygame.K_z:
                        self.player.slide()
                    if event.key == pygame.K_x:
                        self.player.toggle_sword()
                    if event.key == pygame.K_g:
                        self.player.attack(1)
                    if event.key == pygame.K_h:
                        self.player.attack(2)
                    if event.key == pygame.K_k:
                        self.player.player_die()
                    if event.key == pygame.K_t:
                        self.player.decreaseHealth()
                    if event.key == pygame.K_y:
                        self.player.increaseHealth()
                    if event.key == pygame.K_u:
                        self.player.useBow()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_u:
                        self.player.releaseBow()
                    if event.key == pygame.K_a or event.key == pygame.K_d:
                        self.player.isMoving = False
                    if event.key == pygame.K_s:
                        self.player.isCrouching = False
                        self.isMoving = False
                        self.isCrouching = True
                        self.isStretchingBow = False
                        self.usingBow = False

            # key combination for special attack
            # quite hacky but works
            keyPress = pygame.key.get_pressed()
            if keyPress[pygame.K_g] and keyPress[pygame.K_h]:
                if self.player.spinStrength > 0.5:
                    self.player.attack(3)
                    self.player.spinStrength -= 0.7

            self.update()
            self.draw()

            self.clock.tick(FPS)

    def update(self):
        self.spriteGroup.update(self.dt, self.screen)

    def draw(self):
        self.screen.fill(BLACK)

        for sprite in self.spriteGroup.sprites():
            if sprite.base_type == 'heart':
                sprite.draw(self.screen)
        
        self.player.update(self.dt)
        self.player.draw(self.screen)

        self.screen.blit(self.renderFont(self.clock.get_fps()), (300,0))

        pygame.display.update()