"""
Debug game class module
author: Joshua Akangah
date: 13/8/20
"""

from CONFIG.settings import *
from GLOBAL.functions import *

class Game:
    def __init__(self):
        self.entities = []
        self.isRunning = True
        self.screen = pygame.display.set_mode(SCREEN_SIZE, pygame.RESIZABLE)
        self.display = pygame.Surface(DISPLAY_SIZE)
        self.trueScroll = [0, 0]
        self.scroll = [0, 0]
        self.parallaxObjects = []
        self.tileRects = []
        self.map = {}
        self.tileIndex = {
            1: pygame.Surface((16, 16)),
            2: pygame.Surface((16, 16)),
            3: pygame.Surface((16, 16)),
        }
        
        # game clock
        self.clock = CLOCK

        # fonts
        self.font = pygame.font.SysFont('Arial', 16, 2)

        # filling tiles
        self.tileIndex.get(1).fill(RED)
        self.tileIndex.get(2).fill(GREEN)
        self.tileIndex.get(3).fill(BLUE)

        # temp player movement
        self.playerMovement = [0, 0]
        self.playerMomentum = 0
        self.playerSurf = pygame.Surface((10, 25))
        self.playerRight = False
        self.playerLeft = False
        self.playerSurf.fill(WHITE)
        self.playerRect = self.playerSurf.get_rect()

        # temp anim
        self.player = None

        self.time_epoch = time.time()
        self.dt = time.time() - self.time_epoch

    @staticmethod
    def setBiome(biome):
        pass

    @staticmethod
    def setParallax(objects):
        pass
        
    # function for chunk generating in world
    def generate_chunk(self, x, y):
        chunk_data = []
        for y_pos in range(CHUNK_SIZE):
            for x_pos in range(CHUNK_SIZE):
                target_x = x * CHUNK_SIZE + x_pos
                target_y = y * CHUNK_SIZE + y_pos

                tile_type = 0
                
                # using perlin noise for random terrain generation
                height = int(noise.pnoise1(target_x*0.1, repeat=9999999) * 5)
                if target_y > (8 - height):
                    tile_type = 2 # dirt
                elif target_y == 8 - height:
                    tile_type = 1 # grass
                elif target_y == 8 - height - 1:
                    if random.randint(1, 5) == 1:
                        # randomly place grass
                        tile_type = 3 
                if tile_type != 0:
                    chunk_data.append([[target_x, target_y], tile_type])

        return chunk_data

    def update(self, dt):
        if self.player != None:
            self.player.update(self.dt)

        pygame.display.update()

    def draw(self):
        self.tileRects = []

        for y in range(3):
            for x in range(4):
                target_x = x - 1 + int(round(self.trueScroll[0]/(CHUNK_SIZE*16)))
                target_y = y - 1 + int(round(self.trueScroll[1]/(CHUNK_SIZE*16)))
                target_chunk = str(target_x) + ';' + str(target_y)

                if target_chunk not in self.map:
                    self.map[target_chunk] = self.generate_chunk(target_x, target_y)

                for tile in self.map[target_chunk]:
                    self.display.blit(self.tileIndex.get(tile[1]), (tile[0][0]*16-self.trueScroll[0], tile[0][1]*16-self.trueScroll[1]))

                    if tile[1] in [1, 2]:
                        self.tileRects.append(pygame.Rect(tile[0][0]*16,tile[0][1]*16,16,16))

        self.display.blit(self.playerSurf, (self.playerRect.x-self.scroll[0], self.playerRect.y-self.scroll[1]))

        # draw player
        if self.player != None:
            self.player.draw(self.display)

        self.screen.blit(pygame.transform.scale(self.display, SCREEN_SIZE), (0, 0))
        self.screen.blit(self.renderFps(self.clock.get_fps()), (540,0))

    def renderFps(self, fps):
        return self.font.render(f"FPS: {round(fps)}", 0, GREEN)

    def handleEvent(self):
        # event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    self.playerRight = True
                    self.playerLeft = False
                if event.key == pygame.K_a:
                    self.playerLeft = True
                    self.playerRight = False
                if event.key == pygame.K_w:
                    self.playerMomentum = -5
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    self.playerRight = False
                if event.key == pygame.K_a:
                    self.playerLeft = False

            if event.type == pygame.VIDEORESIZE:
                global SCREEN_SIZE
                SCREEN_SIZE = (event.w, event.h)
                self.screen = pygame.display.set_mode(SCREEN_SIZE, pygame.RESIZABLE)

    def mainLoop(self):
        # main game loop
        while self.isRunning:
            self.dt = time.time() - self.time_epoch

            self.dt *= FPS

            self.time_epoch = time.time()

            # screen scrolling
            self.trueScroll[0] += (self.playerRect.x - self.trueScroll[0]-152)/20
            self.trueScroll[1] += (self.playerRect.y - self.trueScroll[1]-106)/20
            self.scroll = self.trueScroll.copy()
            self.scroll[0] = int(self.scroll[0])
            self.scroll[1] = int(self.scroll[1])

            self.handleEvent()

            self.display.fill(BLACK)

            # player movement
            self.playerMovement = [0, 0]
            if self.playerRight:
                self.playerMovement[0] += 2
            if self.playerLeft:
                self.playerMovement[0] -= 2
            self.playerMovement[1] += self.playerMomentum
            self.playerMomentum += 0.2
            if self.playerMomentum > 3:
                self.playerMomentum = 3

            # player collision
            self.playerRect, collisions = move(self.playerRect, self.playerMovement, self.tileRects)

            if collisions.get('bottom'):
                self.playerMomentum = 0
                self.player.stopFalling()

            self.update(self.dt)
            self.draw()

            # print(self.playerRight)
            # print(self.playerLeft)
           
            self.clock.tick(FPS)
