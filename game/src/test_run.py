from PLAYER.load_sprites import *
from PLAYER.animation import *
from PLAYER.settings import *
from PLAYER.sprite import *

screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)

running = True

# test objects
player = Player()

while running:
	CLOCK.tick(FPS)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill(BLACK)

	player.update(DT)
	player.draw(screen)

	pygame.display.update()