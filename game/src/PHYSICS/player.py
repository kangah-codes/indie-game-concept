"""
	Physics object for player
	author: Joshua Akangah
	date: 10/8/20
"""

from CONFIG.settings import *

class PlayerPhysics():
	def __init__(self, x, y):
		self.mass = 1
		self.accelX = 0
		self.accelY = 800
		self.velX = 0
		self.velY = 0
		self.moment = 0
		self.friction = .9
		self.pos = pygame.math.Vector2(x, y)
		self.isJumping = False
		self.isFalling = True

	def simulateGravity(self):
		if self.isFalling or self.isJumping:
			self.pos.y += self.velY * (30/1000.0)
			self.velY += self.accelY * (30/1000.0)

			if self.velY >= 0:
				self.isJumping = False
				self.isFalling = True

			elif self.velY < 0:
				self.isJumping = True
				self.isFalling = False

	