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
		self.space = pymunk.Space()
		self.space.gravity = pymunk.Vec2d(0.0, -900.0)

		self.spriteGroup = pygame.sprite.Group()

	def run(self):
		while self.running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
					pygame.quit()
					exit()

			self.dt = self.clock.tick(30)/1000.0
			self.runLogic()
			self.draw()

	def runLogic(self):
		self.space.step(1/60)
		self.spriteGroup.update(self.dt, self.screen)

	def draw(self):
		self.screen.fill(BLACK)

		self.spriteGroup.draw(self.screen)

		for sprite in self.spriteGroup:
			shape = sprite.shape
			ps = [pos.rotated(shape.body.angle) + shape.body.position for pos in shape.get_vertices()]
			ps = [pymunk.pygame_util.to_pygame(pos, self.screen) for pos in ps]
			ps += [ps[0]]
			#self.screen.blit(sprite.image, pymunk.pygame_util.to_pygame(sprite.shape.body.position, self.screen))
			pygame.draw.lines(self.screen, (RED), False, ps, 1)

		pygame.display.update()