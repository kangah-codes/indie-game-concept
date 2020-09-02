"""
Game manager script
"""

from CONFIG.settings import *
from GLOBAL.functions import *

class GameManager():
    def __init__(self):
        self.camera = None
        self.entities = []
        self.display = None
        self.cameraPos = [0, 0]
        self.trueCameraPos = [0, 0]
        self.font = None
        self.player = None

        self.screen = pygame.display.set_mode(SCREEN_SIZE, pygame.RESIZABLE)
        self.display = pygame.Surface(DISPLAY_SIZE)

        self.time_epoch = time.time()
        self.dt = time.time() - self.time_epoch

        self.isRunning = True

    def update(self, dt):
        self.dt = time.time() - self.time_epoch

        self.dt *= FPS

        self.time_epoch = time.time()

        self.player.update(self.dt)

    def draw(self):
        self.display.fill(BLACK)
        self.player.draw(self.display)
        self.screen.blit(pygame.transform.scale(self.display, SCREEN_SIZE), (0, 0))

        pygame.display.update()

    def renderFps(self):
        pass

    def handleEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.isRunning = False
                exit()

            if event.type == pygame.VIDEORESIZE:
                global SCREEN_SIZE
                SCREEN_SIZE = (event.w, event.h)
                self.screen = pygame.display.set_mode(SCREEN_SIZE, pygame.RESIZABLE)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.player.simulateJump()

    def mainLoop(self):
        while self.isRunning:
            self.handleEvent()

            self.update(self.dt)
            self.draw()
