"""
	Physics Object for player
	author: Joshua Akangah
	date: 10/8/20
"""

from .settings import *

class PlayerObject(pygame.sprite.Sprite):
	def __init__(self, space):
		pygame.sprite.Sprite.__init__(self)
		# self.image = pygame.Surface((46, 52))
		# self.image.fill(WHITE)
		# self.originalImage = self.image
		# self.rect = self.image.get_rect()
		self.vertices = [(-23, 26), (23, 26), (23, -26), (0, -26)]
		self.mass = 1
		self.moment = pymunk.moment_for_poly(self.mass, self.vertices)
		self.body = pymunk.Body(self.mass, self.moment)
		self.shape = pymunk.Poly(self.body, self.vertices)
		self.shape.friction = .9
		self.body.position = (150, 600)
		self.space = space
		self.space.add(self.body, self.shape)

	# def update(self, dt, display):
	# 	self.rect = self.image.get_rect()
	# 	self.rect.x, self.rect.y = pymunk.pygame_util.to_pygame(self.body.position, display)
	# 	self.image = pygame.transform.rotate(self.originalImage, math.degrees(self.body.angle))
		