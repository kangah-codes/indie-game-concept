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
        self.screen = pygame.display.set_mode((window_width, window_height))
        self.spriteGroup = pygame.sprite.Group()
        self.playerGroup = []
        self.tiles = None
        self.background = None
        self.font = pygame.font.SysFont('Arial', 16)

        self.time_epoch = time.time()
        self.dt = time.time() - self.time_epoch
        self.map = {}

        self.trueScroll = [0, 0]
        self.scroll = self.trueScroll.copy()

        # self.map = [
        #     ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
        #     ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
        #     ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
        #     ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
        #     ['0','0','0','0','0','0','0','1','1','1','1','1','0','0','0','0','0','0','0'],
        #     ['0','0','0','0','0','0','0','2','2','2','2','2','0','0','0','0','0','0','0'],
        #     ['1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1'],
        #     ['2','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','2'],
        #     ['2','2','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','2','2'],
        #     ['2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2'],
        #     ['2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2'],
        #     ['2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2'],
        #     ['2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2']]

    def renderFont(self, fps):
        return self.font.render(str(round(fps)), 0, GREEN)

    def generate_chunk(self, x, y):
        chunk_data = []
        for y_pos in range(CHUNK_SIZE):
            for x_pos in range(CHUNK_SIZE):
                self.target_x = x * CHUNK_SIZE + x_pos
                self.target_y = y * CHUNK_SIZE + y_pos

                tile_type = 0 # nothing
                if self.target_y > 10:
                    tile_type = 2 # dirt
                elif self.target_y == 10:
                    tile_type = 1 # grass
                elif self.target_y == 9:
                    if random.randint(1,5) == 1:
                        tile_type = 3 # plant
                if tile_type != 0:
                    chunk_data.append([[self.target_x, self.target_y], tile_type])

        return chunk_data

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

            self.update()
            self.draw()

            self.clock.tick(FPS)

    def update(self):
        self.trueScroll[0] += (self.playerGroup[0].rect.x - self.trueScroll[0]-window_width//2)/20
        self.trueScroll[1] += (self.playerGroup[0].rect.y - self.trueScroll[1]-window_height//2)/20
        self.scroll = self.trueScroll.copy()
        self.scroll[0] = int(self.scroll[0])
        self.scroll[1] = int(self.scroll[1])

        self.tile_rects = []
        for y in range(3):
            for x in range(4):
                self.target_x = x - 1 + int(round(self.scroll[0]/(CHUNK_SIZE*16)))
                self.target_y = y - 1 + int(round(self.scroll[1]/(CHUNK_SIZE*16)))
                self.target_chunk = str(self.target_x) + ';' + str(self.target_y)
                
                if self.target_chunk not in self.map:
                    self.map[self.target_chunk] = self.generate_chunk(self.target_x, self.target_y)

                for tile in self.map.get(self.target_chunk):
                    self.screen.blit(self.tiles.tileIndex.get(tile[1]), (tile[0][0]*16 - self.scroll[0], tile[0][1]*16 - self.scroll[1]))
                    if tile[1] in [1,2]:
                        self.tile_rects.append(pygame.Rect(tile[0][0]*16,tile[0][1]*16, 16, 16))

        self.playerGroup[0].collidePlatform(self.tile_rects)
        self.spriteGroup.update(self.dt, self.screen)

    def draw(self):
        self.screen.fill(BLACK)

        if self.tiles != None:
            self.tiles.draw(self.map.get(self.target_chunk), self.screen)
        
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