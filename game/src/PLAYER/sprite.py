"""
	Main player class module
	author: Joshua Akangah
	date: 10/8/20
"""

from .physics import *
from .load_sprites import *
from .animation import *


class Player(PlayerObject):
	def __init__(self, space):
		PlayerObject.__init__(self, space)
		self.current_state = 'idle_no_sword'
		self.animation = PlayerAnimation(player_states.get('idle_no_sword'), 2.0)
		self.image = self.animation.get_current_image()
		self.mask = pygame.mask.from_surface(self.image)
		self.rect = self.image.get_rect()

	def update(self, dt, display):
		self.animation.animate(dt)
		self.image = self.animation.get_current_image()
		self.rect = self.image.get_rect()
		self.mask = pygame.mask.from_surface(self.image)
		self.rect.x, self.rect.y = pymunk.pygame_util.to_pygame(self.body.position, display)
		# self.image = pygame.transform.rotate(self.originalImage, math.degrees(self.body.angle))
