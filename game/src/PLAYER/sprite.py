"""
	Main player class module
	author: Joshua Akangah
	date: 10/8/20
"""

from .load_sprites import *
from .animation import *
from PHYSICS.player import *


class Player(pygame.sprite.Sprite, PlayerPhysics):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		PlayerPhysics.__init__(self, 100, 100)
		self.current_state = 'idle_no_sword'
		self.base_state = 'idle_no_sword'
		self.animation = PlayerAnimation(player_states.get(self.current_state), 2.0)
		self.image = self.animation.get_current_image()
		self.mask = pygame.mask.from_surface(self.image)
		self.rect = self.image.get_rect()
		self.flip = True
		self.dt = FPS*0.00025
		self.holdingSword = False
		self.isRunning = False
		self.isSliding = False
		self.isCrouching = False
		

	def update(self, display):
		if self.pos.y + self.rect.height < 600:
			self.isFalling = True
		else:
			# player is on the ground
			self.isFalling = False
			if self.isRunning:
				# player is currently running
				self.updateState('run')
			else:
				if self.current_state == self.base_state:
					# player is not running or sliding
					self.updateState(self.base_state)
				elif self.current_state == 'crouch':
					self.updateState('crouch')
				else:
					if self.holdingSword:
						self.updateState('idle_sword')

		self.simulateGravity()		
		self.animation.animate(self.dt)
		self.image = self.animation.get_current_image()
		self.rect = self.image.get_rect()
		self.mask = pygame.mask.from_surface(self.image)
		self.vertices = [vertice for vertice in self.mask.outline()]
		self.rect.x, self.rect.y = self.pos.x, self.pos.y
		self.isRunning = False
		self.isSliding = False
		self.isCrouching = False

		# updating states based on player jump or fall
		if self.isJumping:
			self.updateState('jump')
		elif self.isFalling:
			self.updateState('fall')


		# handle movement
		keyPress = pygame.key.get_pressed()

		if keyPress[pygame.K_d]:
			self.isRunning = True
			self.updateState('run')
			self.dt = FPS*0.00025
			self.flip = False
		elif keyPress[pygame.K_a]:
			self.isRunning = True
			self.updateState('run')
			self.dt = FPS*0.00025
			self.flip = True
		elif keyPress[pygame.K_s]:
			self.isCrouching = True
			self.updateState('crouch')


	def drawSword(self):
		self.holdingSword = not self.holdingSword


	def simulateJump(self, speed=-600):
		self.velY = speed
		self.isJumping = True


	def updateState(self, state):
		if self.current_state != state:
			self.current_state = state
			self.animation = PlayerAnimation(player_states.get(self.current_state), 2.0)
			print(self.current_state)

	def draw(self, display):
		if self.flip:
			display.blit(pygame.transform.flip(self.image, True, False), self.pos)
			return
		display.blit(self.image, self.pos)