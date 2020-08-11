"""	
Game object for handling gameplay
author: Joshua Akangah
date: 10/8/20
"""

from .settings import *

class Game:
    def __init__(self):
        self.running = True
        self.clock = CLOCK
        self.screen = pygame.display.set_mode((800, 600))

        # pymunkk stuff
        self.gravity = 9.8

        self.spriteGroup = pygame.sprite.Group()
        self.playerGroup = []
        self.background = None

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.playerGroup[0].perform_jump()
                    if event.key == pygame.K_z:
                        self.playerGroup[0].slide()
                    if event.key == pygame.K_x:
                        self.playerGroup[0].toggle_sword()
                    if event.key == pygame.K_g:
                        self.playerGroup[0].attack(1)
                    if event.key == pygame.K_h:
                        self.playerGroup[0].attack(2)
                    if event.key == pygame.K_k:
                        self.playerGroup[0].player_die()
                    if event.key == pygame.K_t:
                        self.playerGroup[0].decreaseHealth()
                    if event.key == pygame.K_y:
                        self.playerGroup[0].increaseHealth()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_u:
                        self.playerGroup[0].releaseBow()
                    
            # key combination for special attack
            # quite hacky but works
            keyPress = pygame.key.get_pressed()
            if keyPress[pygame.K_g] and keyPress[pygame.K_h]:
                if self.playerGroup[0].spinStrength > 0.5:
                    self.playerGroup[0].attack(3)
                    self.playerGroup[0].spinStrength -= 0.7

            self.dt = self.clock.tick(FPS)/1000.0
            self.runLogic()
            self.draw()

    def runLogic(self):
        self.spriteGroup.update(self.dt, self.screen)


    def draw(self):
        self.screen.fill(BLACK)
        if self.background != None:
            self.background.update(1)
            self.background.background.draw(self.screen)

        # self.spriteGroup.draw(self.screen)
        # do not do this if youre not testing
        for sprite in self.spriteGroup.sprites():
            if sprite.base_type == 'heart':
                sprite.draw(self.screen)

        self.playerGroup[0].update(self.screen)
        self.playerGroup[0].draw(self.screen)

        pygame.display.update()