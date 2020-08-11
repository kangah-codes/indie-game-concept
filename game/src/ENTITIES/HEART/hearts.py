"""
Module for heart entity
author: Joshua Akangah
date: 11/8/20
"""

from ..entity import *
from .settings import *

class HeartSprite(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.base_type = 'heart'
		self.image = images[0]
	
	def setFull(self):
		self.image = images[0]
	
	def setHalf(self):
		self.image = images[1]

	def setEmpty(self):
		self.image = images[2]


class Heart(HeartSprite, Entity):
	def __init__(self, bindedTo):
		HeartSprite.__init__(self)
		Entity.__init__(self)
		self.rect = self.image.get_rect()
		self.player = bindedTo
		self.bars = self.player.health
		self.drawSprites = []

	def update(self, dt, display):
		pass


	def draw(self, display):
		self.drawSprites.clear()
		for heart in self.player.health:
			if heart == 1:
				#print(f"Health at {self.player.health.index(heart)} from full to half")
				self.setFull()
			elif heart == 0.5:
				#print(f"Health at {self.player.health.index(heart)} from half to zero")
				self.setHalf()
			else:
				self.setEmpty()
			self.drawSprites.append(self.image)

		for i in range(len(self.drawSprites)):
			display.blit(self.drawSprites[i], (i*self.rect.width, 100))