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
		self.base_state = 'idle_no_sword' # default player state
		self.current_state = 'idle_no_sword'
		self.pos = pygame.math.Vector2()
		self.image = self.animation.get_current_image()
		self.rect = self.image.get_rect()
		self.mask = pygame.mask.from_surface(self.image)
		self.pos.x, self.pos.y = 100, 100
		self.flip = False
		self.dt = DT


	def update(self, dt):
		self.animation.animate(self.dt)
		self.image = self.animation.get_current_image()
		self.rect = self.image.get_rect()

		# handle keypresses
		keyPress = pygame.key.get_pressed()

		if keyPress[pygame.K_a]:
			self.update_state('run')
			self.current_state = 'run'
			self.dt = FPS*0.00025
			self.flip = True
		elif keyPress[pygame.K_d]:
			self.update_state('run')
			self.current_state = 'run'
			self.dt = FPS*0.00025
			self.flip = False
		else:
			self.update_state(self.base_state)
			self.current_state = self.base_state
			self.dt = FPS*0.0001


	def update_state(self, state):
		if self.current_state != state:
			self.animation = PlayerAnimation(player_states.get(state), 2.0)


	def draw(self, display):
		if self.flip:
			self.image = pygame.transform.flip(self.image, True, False)
		display.blit(self.image, (self.pos.x, self.pos.x))