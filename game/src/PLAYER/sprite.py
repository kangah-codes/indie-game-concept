"""
Main player class module
author: Joshua Akangah
date: 10/8/20
"""

from .load_sprites import *
from .settings import *
from .animation import *
from .physics import *

import time

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
		self.isDoubleJumping = False

		# if player is on ground
		self.onGround = False

		# player is moving
		self.isMoving = False
		self.movingDirection = 1 # horizontal player moving direction 1 for right 0 for left

		# player crouching
		self.isCrouching = False

		# player sliding
		self.isSliding = False

		# holding sword
		self.toggleSword = False

		# attacking
		self.isAttacking = False
		self.attackType = 1
		self.spinStrength = 5

		# die
		self.isDead = False
		
	def update(self, dt):
		if (self.pos.y + self.rect.height >= 600):
			self.pos.y = 600 - self.rect.height
			self.isFalling = False
			self.canDoubleJump = True
			self.onGround = True
			self.jumpCount = 0
			self.isDoubleJumping = False

		# changing on ground state when player is jumping or falling
		if self.isJumping or self.isFalling or self.isDoubleJumping:
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
		if not self.isDead:
			if self.isFalling and not self.isAttacking:
				self.isDoubleJumping = False
				self.update_state('fall')
			elif self.isJumping and not self.isDoubleJumping and not self.isAttacking:
				self.update_state('jump')
			elif self.isMoving and self.onGround and not self.isAttacking:
				# making sure we are on the ground before using the run animation
				self.update_state('run')
			elif self.isCrouching and not self.isAttacking:
				self.update_state('crouch')
			elif self.isSliding and not self.isAttacking:
				self.update_state('slide')
			elif self.toggleSword and not self.isAttacking:
				self.update_state('idle_sword')
			elif self.isDoubleJumping and not self.isAttacking:
				self.state.animate(FPS/2500.0)
				self.update_state('jump_flip')
			elif self.isAttacking:
				self.state.animate(FPS/2000.0)
				if self.attackType == 1:
					self.update_state('attack_1')
				elif self.attackType == 2:
					self.update_state('attack_2')
				else:
					self.update_state('attack_3')
			# checking since player can be on ground even when sliding
			elif self.onGround and not self.isMoving and not self.toggleSword and not self.isAttacking:
				self.update_state(self.base_state)
		else:
			self.update_state('die')
		

		# returning dt to normal when not flipping
		if not self.isDoubleJumping or not self.isAttacking:
			self.dt = FPS/5000.0

		# flipping player based on current move direction
		self.flip = True if self.movingDirection == 0 else False

		self.handleKeypress()

		# stopping sliding animation when last frame is reached
		if self.current_state == 'slide':
			if self.state.is_last_image():
				self.isSliding = False
			else:
				print(self.flip)
				if self.flip:
					self.acc.x = -0.5
				else:
					self.acc.x = 0.5
		
		# apply friction
		self.acc.x += self.vel.x * self.friction

		# equations of motion
		self.vel.x += self.acc.x
		self.pos.x += self.vel.x + 0.5 * self.acc.x

		# making sure we dont go over bounds
		if self.pos.x + self.rect.width > 800:
			self.pos.x = 800 - self.rect.width
		if self.pos.x < 0:
			self.pos.x = 0

		# attacking
		if self.isAttacking:
			if self.state.is_last_image():
				self.isAttacking = False

		# generate
		if self.spinStrength < 5:
			self.spinStrength += 0.005

		# dead
		if self.isDead:
			if self.state.is_last_image():
				time.sleep(1)
				exit()

	
	def attack(self, level):
		self.isAttacking = True
		self.attackType = level
		if self.attackType == 1:
			self.update_state('attack_1')
		elif self.attackType == 2:
			self.update_state('attack_2')
		else:
			self.update_state('attack_3')

	def player_die(self):
		self.isDead = True


	def perform_jump(self, speed=-600):
		if self.canDoubleJump:
			self.jumpCount += 1
			self.vel.y = speed
			self.isJumping = True

			if self.jumpCount >= 1:
				self.update_state('jump_flip')
				self.isDoubleJumping = True

	def slide(self):
		self.isSliding = True

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
		self.toggleSword = not self.toggleSword

	def update_state(self, state):
		if self.current_state != state:
			self.current_state = state
			self.state = PlayerAnimation(player_states.get(self.current_state), 2.0)

	def draw(self, display):
		if self.flip:
			self.image = pygame.transform.flip(self.image, True, False)
		display.blit(self.image, (self.pos.x, self.pos.y))