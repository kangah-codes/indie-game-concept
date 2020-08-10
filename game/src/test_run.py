from PLAYER.load_sprites import *
from PLAYER.animation import *
from PLAYER.settings import *
from PLAYER.sprite import *

# screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
screen = pygame.display.set_mode((800, 600))

running = True

# test objects
player = Player()

while running:
	CLOCK.tick(FPS)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				player.perform_jump()
			if event.key == pygame.K_z:
				player.toggle_sword()

	screen.fill(BLACK)

	player.update(DT)
	player.draw(screen)

	pygame.display.update()