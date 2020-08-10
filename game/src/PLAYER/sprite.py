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
		self.isJumping = False
		self.isFalling = True
		self.isSliding = False
		self.accX, self.accY = 0.0, 800
		self.velX, self.velY = 0.0, 0.0
		self.isDead = False
		self.jumpDisabled = False
		self.canDoubleJump = True
		self.jumpCount = 0


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
			self.breakJump = False


		# handle jumping and falling
		if (self.isFalling or self.isJumping) and (self.pos.y + self.rect.height < 500):
			self.pos.y += self.velY * (30/1000.0)
			self.velY += self.accY * (30/1000.0)

			if self.velY >= 0 and not self.isSliding:
				self.update_state('fall')
				self.current_state = 'fall'
				self.canDoubleJump = False
				self.isFalling = True
			elif self.velY < 0 and not self.isSliding:
				self.update_state('jump')
				self.current_state = 'jump'
				if self.jumpCount < 2:
					self.canDoubleJump = True
				else:
					self.canDoubleJump = False
				self.isJumping = True

        # prevent player from falling off
		if self.pos.y + self.rect.height > 500:
			self.pos.y = 500 - self.rect.height - 1
			self.isFalling = False
			self.isJumping = False
			self.jumpCount = 0

		print(self.canDoubleJump, self.jumpCount)

	def perform_jump(self):
		if not self.isFalling and self.jumpCount < 2:
			self.isJumping = True
			self.dt = FPS*0.00025
			if not self.isJumping or not self.isFalling:
				self.update_state('jump')
				self.current_state = 'jump'
			self.velY = -500
			if self.jumpCount < 2:
				self.jumpCount += 1

			if not self.canDoubleJump:
				return
			else:
				if self.jumpCount < 2:
					self.velY = -500
					self.canDoubleJump = False
					self.jumpCount += 1
			

	def update_state(self, state):
		if self.current_state != state:
			self.animation = PlayerAnimation(player_states.get(state), 2.0)


	def draw(self, display):
		if self.flip:
			self.image = pygame.transform.flip(self.image, True, False)
		display.blit(self.image, (self.pos.x, self.pos.y))