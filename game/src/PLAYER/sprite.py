"""
	Main player class module
	author: Joshua Akangah
	date: 10/8/20
"""

from .load_sprites import *
from .animation import *
from .settings import *

class Player(pygame.sprite.Sprite):
	def __init__(self):
		# load player animation and scale to twice the size
		self.animation = PlayerAnimation(player_states.get('idle_no_sword'), 2.0)
		self.pos = pygame.math.Vector2()
		self.image = self.animation.get_current_image()
		self.rect = self.image.get_rect()
		self.mask = pygame.mask.from_surface(self.image)
		self.pos.x, self.pos.y = 100, 100

	def update(self, dt):
		self.animation.animate(dt)
		self.image = self.animation.get_current_image()
		self.rect = self.image.get_rect()


	def draw(self, display):
		display.blit(self.image, (self.pos.x, self.pos.x))