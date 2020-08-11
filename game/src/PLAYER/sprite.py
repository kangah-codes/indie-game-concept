"""
Main player class module
author: Joshua Akangah
date: 10/8/20
"""

from .load_sprites import *
from .settings import *
from .animation import *
from .physics import *

class Player(pygame.sprite.Sprite, PhysicsObject):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		PhysicsObject.__init__(self, 100, 100)
		# load player animation and scale to twice the size
		self.base_state = 'idle_no_sword'
		self.state = PlayerAnimation(player_states.get('idle_no_sword'), 2.0)
		self.current_state = self.base_state
		self.image = self.state.get_current_image()
		self.rect = self.image.get_rect()
		self.mask = pygame.mask.from_surface(self.image)
		self.dt = FPS/5000.0
		self.flip = False
		self.friction = -0.12

		# handling double jump
		self.jumpCount = 0
		self.canDoubleJump = True

		# if player is on ground
		self.onGround = False

		# player is moving
		self.isMoving = False
		self.movingDirection = 1 # horizontal player moving direction 1 for right 0 for left

		# player crouching
		self.isCrouching = False

		# player sliding
		self.isSliding = False
		
	def update(self, dt):
		if (self.pos.y + self.rect.height >= 600):
			self.pos.y = 600 - self.rect.height
			self.isFalling = False
			self.canDoubleJump = True
			self.onGround = True
			self.jumpCount = 0

		# changing on ground state when player is jumping or falling
		if self.isJumping or self.isFalling:
			self.onGround = False

		self.simulateGravity()
		self.state.animate(self.dt)
		self.image = self.state.get_current_image()
		# compute rect and mask for each frame
		self.rect = self.image.get_rect()
		self.mask = pygame.mask.from_surface(self.image)
		self.rect.x, self.rect.y = self.pos.x, self.pos.y

		# checking if player can double jump
		# i don't know why the first jump count is not added so I made this 1 instead of 2 and it works :)
		if self.jumpCount < 1:
			self.canDoubleJump = True
		else:
			self.canDoubleJump = False

		# updating player states
		if self.isFalling:
			self.update_state('fall')
		elif self.isJumping:
			self.update_state('jump')
		elif self.isMoving:
			self.update_state('run')
		elif self.isCrouching:
			self.update_state('crouch')
		elif self.isSliding:
			self.update_state('slide')
		elif self.onGround and not self.isMoving:
			self.update_state(self.base_state)

		# flipping player based on current move direction
		self.flip = True if self.movingDirection == 0 else False

		self.handleKeypress()

		# stopping sliding animation when last frame is reached
		if self.current_state == 'slide':
			if self.state.is_last_image():
				self.isSliding = False

		# apply friction
		self.acc.x += self.vel.x * self.friction

		# equations of motion
		self.vel.x += self.acc.x
		self.pos.x += self.vel.x + 0.5 * self.acc.x


		if self.pos.x + self.rect.width > 800:
			self.pos.x = 800 - self.rect.width
		if self.pos.x < 0:
			self.pos.x = 0

	def perform_jump(self, speed=-600):
		if self.canDoubleJump:
			self.jumpCount += 1
			self.vel.y = speed
			self.isJumping = True

	def handleKeypress(self):
		keyPress = pygame.key.get_pressed()
		self.acc = pygame.math.Vector2(0, 800)
		if keyPress[pygame.K_a]:
			self.acc.x = -0.5
			self.isMoving = True
			self.movingDirection = 0
		elif keyPress[pygame.K_d]:
			self.acc.x = 0.5
			self.isMoving = True
			self.movingDirection = 1
		elif keyPress[pygame.K_s]:
			self.isMoving = False
			self.isCrouching = True
		else:
			self.isMoving = False
			self.isCrouching = False
		
	def toggle_sword(self):
		pass

	def update_state(self, state):
		if self.current_state != state:
			self.current_state = state
			self.state = PlayerAnimation(player_states.get(self.current_state), 2.0)

	def draw(self, display):
		if self.flip:
			self.image = pygame.transform.flip(self.image, True, False)
		display.blit(self.image, (self.pos.x, self.pos.y))