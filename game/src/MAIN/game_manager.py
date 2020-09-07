"""
Game manager script
"""

from CONFIG.settings import *
from GLOBAL.functions import *
from GLOBAL.font import *

class GameManager():
    def __init__(self):
        self.camera = None
        self.entities = []
        self.enemyEntities = []
        self.display = None
        self.cameraPos = [0, 0]
        self.trueCameraPos = [0, 0]
        self.font = None
        self.player = None

        self.screen = pygame.display.set_mode(SCREEN_SIZE, pygame.RESIZABLE)
        self.display = pygame.Surface(DISPLAY_SIZE)
        self.FONT = generate_font(os.path.join(BASE_DIR, 'assets/UI/FONT/small_font.png'), FONT_DAT, 5, 8, RED)

        self.time_epoch = time.time()
        self.dt = time.time() - self.time_epoch
        self.clock = CLOCK

        self.isRunning = True
        self.font = pygame.font.SysFont('Arial', 16, 2)

    def update(self, dt):
        self.dt = time.time() - self.time_epoch

        self.dt *= FPS

        self.time_epoch = time.time()

        self.player.update(self.dt)

        [entity.update(self.dt, self.player) for entity in self.enemyEntities]

        # collisions
        self.doCollisions()

        self.clock.tick(FPS)

    def draw(self):
        accVel = self.renderAccVel()
        self.display.fill(WHITE)
        self.player.draw(self.display)
        pygame.draw.rect(self.display, BLUE, (self.player.pos.x, self.player.pos.y - 10, self.player.energy_level/5, 5))
        show_text(f'FPS {round(self.clock.get_fps())}', 0, 0, 1, 9999, self.FONT, self.display)
        show_text(accVel[0], 0, 15, 1, 9999, self.FONT, self.display)
        show_text(accVel[1], 0, 30, 1, 9999, self.FONT, self.display)

        [entity.draw(self.display) for entity in self.enemyEntities]

        # for entity in self.enemyEntities:
        #     pygame.draw.line(self.display, BLACK, (entity.rect.centerx, entity.rect.centery), (self.player.rect.centerx, self.player.rect.centery))

        self.screen.blit(pygame.transform.scale(self.display, SCREEN_SIZE), (0, 0))
        pygame.display.update()

    def renderFps(self, fps):
        return self.font.render(f"FPS: {round(fps)}", 0, GREEN)

    def renderAccVel(self):
        return [
            f"Acceleration {self.player.acc}",
            f"Velocity {self.player.vel}"
        ]

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
                # handle player movements
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    self.player.simulateJump()

                # player slide
                if event.key == pygame.K_z:
                    self.player.slide()

                # toggle sword
                if event.key == pygame.K_x:
                    self.player.toggleSword()

                # player attacks
                if event.key == pygame.K_g:
                    if not self.player.is_holding_sword:
                        self.player.punch()
                    else:
                        self.player.attack(1)

                if event.key == pygame.K_h:
                    if not self.player.is_holding_sword:
                        self.player.punch(kick=True)
                    else:
                        self.player.attack(2)

                # cast spell
                if event.key == pygame.K_j:
                    self.player.castSpell()

                # shooting bow
                if event.key == pygame.K_b:
                    self.player.shootBow()

                ## experimental
                ## knock player down
                if event.key == pygame.K_k:
                    self.player.knockDown()


    def mainLoop(self):
        while self.isRunning:
            self.handleEvent()
            self.draw()
            self.update(self.dt)

    def doCollisions(self):
        for enemy in self.enemyEntities:
            if pygame.sprite.collide_mask(enemy, self.player):
                print("COLLIDE")
