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
		self.base_state = 'slide'
		self.state = PlayerAnimation(player_states.get(self.base_state), 2.0)
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

		# get current tick
		self.dt = dt

		print(self.rect.height+self.pos.y)

		if (self.pos.y + self.rect.height >= window_height):
			self.pos.y = window_height - self.rect.height
			self.isFalling = False
			self.canDoubleJump = True
			self.onGround = True
			self.jumpCount = 0
			self.isDoubleJumping = False


		# changing on ground state when player is jumping or falling
		if self.isJumping or self.isFalling or self.isDoubleJumping:
			self.onGround = False

		self.simulateGravity(self.dt)

		# stretching bow
		if self.isStretchingBow:
			self.state.animate(self.dt, True)
		else:
			self.state.animate(self.dt)

		# print(self.rect.height)

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


		# making sure we dont go over bounds
		if self.pos.x + self.rect.width > screen_width:
			self.pos.x = screen_width - self.rect.width
		if self.pos.x < 0:
			self.pos.x = 0

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
			self.state = PlayerAnimation(player_states.get(self.current_state), 2.0)

	def draw(self, display):
		self.drawSurf.fill(BLACK)
		
		for i in self.mask.outline():
			pygame.draw.circle(self.drawSurf, WHITE, i, 1)

		if self.flip:
			self.image = pygame.transform.flip(self.image, True, False)
			self.drawSurf = pygame.transform.flip(self.drawSurf, True, False)
		
		#display.blit(self.drawSurf, (self.rect.x, self.rect.y))
		
		display.blit(self.image, (self.pos.x, self.pos.y))

	def collidePlatform(self, platforms, ramps=[]):
		block_hit_list = collision_test(self.rect, platforms)
		collision_types = {'top':False,'bottom':False,'right':False,'left':False,'slant_bottom':False,'data':[]}

		# added collision data to "collision_types". ignore the poorly chosen variable name
		for block in block_hit_list:
			markers = [False,False,False,False]
			if not self.flip:
				self.rect.right = block.left
				collision_types['right'] = True
				markers[0] = True
			elif self.flip:
				self.rect.left = block.right
				collision_types['left'] = True
				markers[1] = True
			collision_types['data'].append([block, markers])
			self.pos.x = self.rect.x
			
		block_hit_list = collision_test(self.rect, platforms)
		for block in block_hit_list:
			markers = [False,False,False,False]
			if self.acc.y > 0:
				self.rect.bottom = block.top
				collision_types['bottom'] = True
				markers[2] = True
			elif self.acc.y < 0:
				self.rect.top = block.bottom
				collision_types['top'] = True
				markers[3] = True

			collision_types['data'].append([block, markers])

			self.pos.y = self.rect.y
			#self.pos.x = self.rect.x
			self.isFalling = False
			self.onGround = True
			self.canDoubleJump = True
			self.onGround = True
			self.jumpCount = 0
			self.isDoubleJumping = False

			

		return collision_types
