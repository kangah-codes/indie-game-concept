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
        self.spriteGroup = pygame.sprite.Group()
        self.playerGroup = []
        self.tiles = []
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
                    if event.key == pygame.K_a and not self.playerGroup[0].usingBow:
                        self.playerGroup[0].isMoving = True
                        self.playerGroup[0].movingDirection = 0
                        self.playerGroup[0].isStretchingBow = False
                        self.playerGroup[0].usingBow = False
                    if event.key == pygame.K_d and not self.playerGroup[0].usingBow:
                        self.playerGroup[0].isMoving = True
                        self.playerGroup[0].movingDirection = 1
                        self.playerGroup[0].isStretchingBow = False
                        self.playerGroup[0].usingBow = False
                    if event.key == pygame.K_s:
                        self.playerGroup[0].isCrouching = True
                        self.isMoving = False
                        self.isCrouching = True
                        self.isStretchingBow = False
                        self.usingBow = False
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
                    if event.key == pygame.K_u:
                        self.playerGroup[0].useBow()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_u:
                        self.playerGroup[0].releaseBow()
                    if event.key == pygame.K_a or event.key == pygame.K_d:
                        self.playerGroup[0].isMoving = False
                    if event.key == pygame.K_s:
                        self.playerGroup[0].isCrouching = False
                        self.isMoving = False
                        self.isCrouching = True
                        self.isStretchingBow = False
                        self.usingBow = False

            # key combination for special attack
            # quite hacky but works
            keyPress = pygame.key.get_pressed()
            if keyPress[pygame.K_g] and keyPress[pygame.K_h]:
                if self.playerGroup[0].spinStrength > 0.5:
                    self.playerGroup[0].attack(3)
                    self.playerGroup[0].spinStrength -= 0.7

            self.runLogic()
            self.draw()

            self.clock.tick(FPS)

    def runLogic(self):
        self.spriteGroup.update(self.dt, self.screen)

    def draw(self):
        self.screen.fill(BLACK)
        
        if self.background != None:
            self.background.update(1)
            self.background.background.draw(self.screen)

        for sprite in self.spriteGroup.sprites():
            if sprite.base_type == 'heart':
                sprite.draw(self.screen)

        self.playerGroup[0].update(self.dt)
        self.playerGroup[0].draw(self.screen)

        self.screen.blit(self.renderFont(self.clock.get_fps()), (700, 0))

        pygame.display.update()