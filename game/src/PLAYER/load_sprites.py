"""
	Module for handling loading of player sprites
	author: Joshua Akangah
    date: 10/9/20
"""

from .settings import *

# Using a dictionary to store player states
# It is easier this way since we can quickly switch through player states using strings as keys

player_states = {
	'idle_no_sword': [
		os.path.join(BASE_DIR, 'assets/PLAYER/IDLE/NO_SWORD/idle1.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/IDLE/NO_SWORD/idle2.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/IDLE/NO_SWORD/idle3.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/IDLE/NO_SWORD/idle4.png'),
	],
	'idle_sword': [
		os.path.join(BASE_DIR, 'assets/PLAYER/IDLE/WITH_SWORD/idle_sword_1.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/IDLE/WITH_SWORD/idle_sword_2.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/IDLE/WITH_SWORD/idle_sword_3.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/IDLE/WITH_SWORD/idle_sword_4.png'),
	],
	'jump': [
		os.path.join(BASE_DIR, 'assets/PLAYER/JUMP/jump_1.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/JUMP/jump_2.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/JUMP/jump_3.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/JUMP/jump_4.png'),
	],
	'jump_flip': [
		os.path.join(BASE_DIR, 'assets/PLAYER/JUMP_FLIP/flip_1.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/JUMP_FLIP/flip_2.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/JUMP_FLIP/flip_3.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/JUMP_FLIP/flip_4.png'),
	],
	'run': [
		os.path.join(BASE_DIR, 'assets/PLAYER/RUN/run_1.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/RUN/run_2.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/RUN/run_3.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/RUN/run_4.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/RUN/run_5.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/RUN/run_6.png'),
	],
	'slide': [
		os.path.join(BASE_DIR, 'assets/PLAYER/SLIDE/slide_1.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/SLIDE/slide_2.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/SLIDE/slide_3.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/SLIDE/slide_4.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/SLIDE/slide_5.png'),
	],
	'attack_1': [
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/ATTACK_1/attack_1_1.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/ATTACK_1/attack_1_2.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/ATTACK_1/attack_1_3.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/ATTACK_1/attack_1_4.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/ATTACK_1/attack_1_5.png'),
	],
	'attack_2': [
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/ATTACK_2/attack_2_1.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/ATTACK_2/attack_2_2.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/ATTACK_2/attack_2_3.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/ATTACK_2/attack_2_4.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/ATTACK_2/attack_2_5.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/ATTACK_2/attack_2_6.png'),
	],
	'attack_3': [
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/ATTACK_3/attack_3_1.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/ATTACK_3/attack_3_2.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/ATTACK_3/attack_3_3.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/ATTACK_3/attack_3_4.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/ATTACK_3/attack_3_5.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/ATTACK_3/attack_3_6.png'),
	],
	'shoot_bow_standing': [
		os.path.join(BASE_DIR, 'assets/PLAYER/BOW/SHOOT_STAND/1.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/BOW/SHOOT_STAND/2.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/BOW/SHOOT_STAND/3.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/BOW/SHOOT_STAND/4.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/BOW/SHOOT_STAND/5.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/BOW/SHOOT_STAND/6.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/BOW/SHOOT_STAND/7.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/BOW/SHOOT_STAND/8.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/BOW/SHOOT_STAND/9.png'),
	],
	'shoot_bow_jumping': [
		os.path.join(BASE_DIR, 'assets/PLAYER/BOW/SHOOT_JUMP/1.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/BOW/SHOOT_JUMP/2.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/BOW/SHOOT_JUMP/3.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/BOW/SHOOT_JUMP/4.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/BOW/SHOOT_JUMP/5.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/BOW/SHOOT_JUMP/6.png'),
	],
	'climb': [
		os.path.join(BASE_DIR, 'assets/PLAYER/CLIMB/0.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/CLIMB/1.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/CLIMB/2.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/CLIMB/3.png'),
	],
	'fall': [
		os.path.join(BASE_DIR, 'assets/PLAYER/FALL/fall_1.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/FALL/fall_2.png'),
	],
	'hurt': [
		os.path.join(BASE_DIR, 'assets/PLAYER/HURT/hurt_1.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/HURT/hurt_2.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/HURT/hurt_3.png'),
	],
	'crouch': [
		os.path.join(BASE_DIR, 'assets/PLAYER/CROUCH/crouch1.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/CROUCH/crouch2.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/CROUCH/crouch3.png'),
	],
	'die': [
		os.path.join(BASE_DIR, 'assets/PLAYER/DIE/die_1.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/DIE/die_2.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/DIE/die_3.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/DIE/die_4.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/DIE/die_5.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/DIE/die_6.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/DIE/die_7.png'),
	]
}
