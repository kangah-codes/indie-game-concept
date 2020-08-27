"""
Debug game class module
author: Joshua Akangah
date: 13/8/20
"""

from CONFIG.settings import *
from GLOBAL.functions import *
from WORLD.backgrounds import *
from WORLD.parallax import *

class Game:
    def __init__(self):
        self.entities = []
        self.isRunning = True
        self.screen = pygame.display.set_mode(SCREEN_SIZE, pygame.RESIZABLE)
        self.display = pygame.Surface(DISPLAY_SIZE)
        self.trueScroll = [0, 0]
        self.scroll = [0, 0]
        self.parallaxObjects = [
            Background(clouds.get(5), (0, 20)),
            Background(clouds.get(3), (0, -10)),
            Background(clouds.get(4), (0, -10))
        ]

        self.tileRects = []
        self.map = {}
        # temporary tiles
        self.tileIndex = snow_tiles

        self.tileIndex.get(3).set_colorkey(WHITE)

        # game clock
        self.clock = CLOCK

        # fonts
        self.font = pygame.font.SysFont('Arial', 16, 2)

        # temp player movement
        self.playerMovement = [0, 0]
        self.playerMomentum = 0
        self.playerSurf = pygame.Surface((15, 45))
        self.playerRight = False
        self.playerLeft = False
        self.playerSurf.fill(WHITE)
        self.playerRect = self.playerSurf.get_rect()

        self.time_epoch = time.time()
        self.dt = time.time() - self.time_epoch

        self.seedGenerator = random.choice([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])

        self.biome = 'forest'
        self.backgroundObjects = [
            [0.25,[0,0,10,400]],
            [0.25,[280,30,40,400]],
            [0.5,[30,40,40,400]],
            [0.5,[130,90,100,400]],
            [0.5,[300,80,120,400]],
        ]

        self.background = None

    def update(self, dt):
        for background in self.parallaxObjects:
            background.update()

        pygame.display.update()

    def draw(self):
        self.display.blit(forest_background.get(1), (0, 0))

        self.display.blit(snow_mountains.get(1), (0, 10))

        for background in self.parallaxObjects:
            background.draw(self.display)

        for background_object in self.backgroundObjects:
            obj_rect = pygame.Rect(background_object[1][0]-self.scroll[0]*background_object[0],background_object[1][1]-self.scroll[1]*background_object[0],background_object[1][2],background_object[1][3])
            if background_object[0] == 0.5:
                pygame.draw.rect(self.display,(14,222,150),obj_rect)
            else:
                pygame.draw.rect(self.display,(9,91,85),obj_rect)


        self.tileRects = []

        for y in range(3):
            for x in range(4):
                target_x = x - 1 + int(round(self.trueScroll[0]/(CHUNK_SIZE*16)))
                target_y = y - 1 + int(round(self.trueScroll[1]/(CHUNK_SIZE*16)))
                target_chunk = str(target_x) + ';' + str(target_y)

                if target_chunk not in self.map:
                    self.map[target_chunk] = generate_chunk(target_x, target_y)

                for tile in self.map[target_chunk]:
                    if tile[1] == 4:
                        self.display.blit(self.tileIndex.get(tile[1]), (tile[0][0]*16-self.trueScroll[0]-16, tile[0][1]*16-self.trueScroll[1]-16))
                    else:
                        self.display.blit(self.tileIndex.get(tile[1]), (tile[0][0]*16-self.trueScroll[0], tile[0][1]*16-self.trueScroll[1]))

                    if tile[1] in [1, 2]:
                        self.tileRects.append(pygame.Rect(tile[0][0]*16,tile[0][1]*16, 16, 16))

        self.display.blit(self.playerSurf, (self.playerRect.x-self.scroll[0], self.playerRect.y-self.scroll[1]))

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

            # player collisions
            self.playerRect, collisions = move(self.playerRect, self.playerMovement, self.tileRects)

            # screen scrolling
            self.trueScroll[0] += (self.playerRect.x - self.trueScroll[0]-152)/20
            self.trueScroll[1] += (self.playerRect.y - self.trueScroll[1]-106)/20
            self.scroll = self.trueScroll.copy()
            self.scroll[0] = int(self.scroll[0])
            self.scroll[1] = int(self.scroll[1])

            self.handleEvent()

            # player movement
            self.playerMovement = [0, 0]
            if self.playerRight:
                self.playerMovement[0] += 2

            if self.playerLeft:
                self.playerMovement[0] -= 2

            if self.playerLeft or self.playerRight:
                if collisions.get('right') != True and collisions.get('left') != True:
                    multiplier = 0.5
                    for background in self.parallaxObjects[::-1]:
                        background.move(-self.playerMovement[0]/3*multiplier)
                        multiplier *= .5

            self.playerMovement[1] += self.playerMomentum
            self.playerMomentum += 0.2
            if self.playerMomentum > 3:
                self.playerMomentum = 3

            if collisions.get('bottom'):
                self.playerMomentum = 0

            self.update(self.dt)
            self.draw()

            self.clock.tick(FPS)
