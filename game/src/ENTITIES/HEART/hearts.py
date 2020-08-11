"""
Module for heart entity
author: Joshua Akangah
date: 11/8/20
"""

from ..entity import *
from .settings import *

class Heart(pygame.sprite.Sprite, Entity):
	def __init__(self, binded_to):
		pygame.sprite.Sprite.__init__(self)
		Entity.__init__(self)
		# selecting a parent entity's life to display
		self.parentEntity = binded_to
		# selecting loaded heart sprites
		self.images = images
		# setting default image to first
		self.image = self.images[0]
		self.halfImage = self.images[1]
		self.emptyImage = self.images[2]
		self.pos = pygame.math.Vector2(100, 100)
		self.fullLife = self.parentEntity.fullLife
		self.parentLife = self.parentEntity.life
		self.type = 'heart'
		self.drawnLife = []

	def update(self, dt, display):
		self.rect = self.image.get_rect()
		self.rect.x, self.rect.y = self.pos.x, self.pos.y

	def draw(self, display):
		for i in range(self.fullLife):
			for j in range(self.parentLife):
				display.blit(self.image, (i*self.rect.width+10, self.pos.y))
				self.drawnLife.append(self.image)
			for k in range(self.fullLife-self.parentLife):
				display.blit(self.emptyImage, (j*self.rect.width+10, self.pos.y))
		print(self.drawnLife)

