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
		self.state = PlayerAnimation(player_states.get(self.base_state), 1.3)
		self.current_state = self.base_state
		self.image = self.state.get_current_image()
		self.rect = self.image.get_rect()
		self.mask = pygame.mask.from_surface(self.image)

		self.flip = False
		# using array to store player heart states
		# 1 is full, 0.5 is half, 0 is empty
		self.health = [1, 1, 1, 1, 1]

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
		self.isDrawingSword = False
		self.isPuttingBackSword = False
		self.toggleSword = False

		# attacking
		self.isAttacking = False
		self.attackType = 1
		self.spinStrength = 5

		# die
		self.isDead = False
		self.life = 3
		self.fullLife = 5

		# inventory
		self.arrows = 5
		self.usingBow = False
		self.isStretchingBow = False
		self.isReleasingBow = False

		self.collisions = None
		self.collisionTypes = {'top':False,'bottom':False,'right':False,'left':False}

		self.drawSurf = pygame.Surface((self.rect.width, self.rect.height))

	def releaseBow(self):
		self.isStretchingBow = False
		self.isReleasingBow = True

	def stopFalling(self):
		self.isFalling = False
		self.canDoubleJump = True
		self.onGround = True
		self.jumpCount = 0
		self.isDoubleJumping = False

	def decreaseHealth(self):
		# minus health
		for i in range(len(self.health)-1, -1, -1):
			if self.health[i] == 0:
				continue
			elif self.health[i] == 0.5:
				# bring from half to empty
				self.health[i] = 0
				break
			else:
				# bring from full to half
				self.health[i] = 0.5
				break
		
		# checking if player life is empty
		if all(heart == self.health[0] for heart in self.health):
			self.player_die()

	def increaseHealth(self):
		# increase
		for i in range(len(self.health)):
			if self.health[i] == 0:
				self.health[i] = 0.5
				break
			elif self.health[i] == 0.5:
				# bring from half to empty
				self.health[i] = 1
				break
			else:
				# bring from full to half
				continue
		
	def update(self, dt):
		self.image = self.state.get_current_image()

		# compute rect and mask for each frame
		self.rect = self.image.get_rect()
		self.mask = pygame.mask.from_surface(self.image)
		self.rect.x, self.rect.y = self.pos

		print(self.mask.get_size())

		# get current tick
		self.dt = dt

		if (self.pos.y + self.rect.height >= DISPLAY_SIZE[1]):
			self.pos.y = DISPLAY_SIZE[1] - self.rect.height
			self.stopFalling

		# changing on ground state when player is jumping or falling
		if self.isJumping or self.isFalling or self.isDoubleJumping:
			self.onGround = False

		self.simulateGravity(self.dt)

		# stretching bow
		if self.isStretchingBow:
			self.state.animate(self.dt, True)
		else:
			self.state.animate(self.dt)


		# checking if player can double jump
		# i don't know why the first jump count is not added so I made this 1 instead of 2 and it works :)
		if self.jumpCount < 1:
			self.canDoubleJump = True
		else:
			self.canDoubleJump = False

		# player movement
		if self.isMoving:
			self.move(self.speed)

		# updating player states
		if not self.isDead:
			if self.isFalling \
				and not self.isAttacking \
				and not self.isDrawingSword \
				and not self.usingBow \
				and not self.isReleasingBow \
				and not self.isPuttingBackSword:
				self.isDoubleJumping = False
				self.update_state('fall')
			elif self.isJumping \
				and not self.isDoubleJumping \
				and not self.isAttacking \
				and not self.isDrawingSword \
				and not self.isReleasingBow \
				and not self.usingBow \
				and not self.isPuttingBackSword:
				self.update_state('jump')
			elif self.isMoving \
				and self.onGround \
				and not self.isAttacking \
				and not self.isDrawingSword \
				and not self.usingBow \
				and not self.isReleasingBow \
				and not self.isPuttingBackSword:
				# making sure we are on the ground before using the run animation
				self.update_state('run')
			elif self.isCrouching\
				and not self.isAttacking \
				and not self.isDrawingSword \
				and not self.usingBow \
				and not self.isReleasingBow \
				and not self.isPuttingBackSword:
				self.update_state('crouch')
			elif self.isSliding \
				and not self.isAttacking \
				and not self.isDrawingSword \
				and not self.usingBow \
				and not self.isReleasingBow \
				and not self.isPuttingBackSword:
				self.update_state('slide')
			elif self.toggleSword \
				and not self.isAttacking \
				and not self.isDrawingSword \
				and not self.usingBow \
				and not self.isReleasingBow \
				and not self.isPuttingBackSword:
				self.update_state('idle_sword')
			elif self.isDoubleJumping \
				and not self.isAttacking \
				and not self.isDrawingSword \
				and not self.usingBow \
				and not self.isReleasingBow \
				and not self.isPuttingBackSword:
				self.state.animate(self.dt)
				self.update_state('jump_flip')
			elif self.isAttacking\
				and not self.isDrawingSword \
				and not self.usingBow \
				and not self.isReleasingBow \
				and not self.isPuttingBackSword:
				self.state.animate(self.dt)
				if self.attackType == 1:
					self.update_state('attack_1')
				elif self.attackType == 2:
					self.update_state('attack_2')
				else:
					self.update_state('attack_3')
			# checking since player can be on ground even when sliding
			elif self.onGround \
				and not self.isMoving \
				and not self.toggleSword \
				and not self.isAttacking \
				and not self.usingBow \
				and not self.isStretchingBow \
				and not self.isReleasingBow \
				and not self.isPuttingBackSword:
				self.update_state(self.base_state)
			elif self.isDrawingSword \
				and not self.isReleasingBow \
				and not self.usingBow:
				self.state.animate(self.dt*0.5)
				self.update_state('draw_sword')
			elif self.isPuttingBackSword \
				and not self.isReleasingBow \
				and not self.usingBow:
				self.state.animate(self.dt*0.5)
				self.update_state('put_back')
			elif self.usingBow:
				if not self.isStretchingBow \
					and not self.isReleasingBow:
					if self.onGround:
						self.update_state('shoot_stand')
				elif self.isStretchingBow \
					and not self.isReleasingBow:
					self.update_state('hold_bow')
				elif not self.isStretchingBow \
					and self.isReleasingBow:
					self.state.animate(self.dt*0.25)
					# release whether player is still stretching or not
					self.update_state('release_bow')
				
		else:
			self.update_state('die')

		# flipping player based on current move direction
		self.flip = True if self.movingDirection == 0 else False

		# stopping sliding animation when last frame is reached
		if self.current_state == 'slide':
			if self.state.is_last_image():
				self.isSliding = False
			self.move(self.speed)
		
		# apply friction
		# self.acc.x += self.vel.x * self.friction * (self.dt/FPS*2)

		# # equations of motion
		# self.vel.x += self.acc.x * (self.dt/FPS*2)
		# self.pos.x += self.vel.x + 0.5 * self.acc.x

		# attacking
		if self.isAttacking:
			if self.state.is_last_image():
				self.isAttacking = False

		# using bow
		if self.usingBow:
			if not self.isReleasingBow:
				if self.state.is_last_image():
					self.usingBow = True
					self.isStretchingBow = True
				else:
					self.isStretchingBow = False
			else:
				if self.state.is_last_image():
					self.usingBow = False
				self.isStretchingBow = False
			
		if self.isReleasingBow:
			if self.state.is_last_image():
				self.isReleasingBow = False

		# generate
		if self.spinStrength < 5:
			self.spinStrength += 0.005

		# dead
		if self.isDead:
			if self.state.is_last_image():
				exit()

		# draw sword animations
		if self.isDrawingSword:
			if self.state.is_last_image():
				self.isDrawingSword = False
		
		if self.isPuttingBackSword:
			if self.state.is_last_image():
				self.isPuttingBackSword = False

	
	def attack(self, level):
		if self.toggleSword:
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

	def useBow(self):
		if not self.toggleSword:
			# making sure player is not using sword first
			self.usingBow = True

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

	def move(self, accel):
		if self.flip:
			self.pos.x -= accel
		else:
			self.pos.x += accel
		
	def toggle_sword(self):
		self.toggleSword = not self.toggleSword

		if self.toggleSword:
			self.update_state('draw_sword')
			self.isDrawingSword = True
			self.isPuttingBackSword = False
		else:
			self.update_state('put_back')
			self.isPuttingBackSword = True
			self.isDrawingSword = False

	def update_state(self, state):
		if self.current_state != state:
			self.current_state = state
			self.state = PlayerAnimation(player_states.get(self.current_state), 1.3)

	def draw(self, display):		
		for i in self.mask.outline():
			pygame.draw.circle(self.drawSurf, WHITE, i, 1)

		if self.flip:
			self.image = pygame.transform.flip(self.image, True, False)
			self.drawSurf = pygame.transform.flip(self.drawSurf, True, False)