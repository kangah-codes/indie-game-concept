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
		os.path.join(BASE_DIR, 'assets/PLAYER/IDLE/NO_SWORD/0.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/IDLE/NO_SWORD/1.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/IDLE/NO_SWORD/2.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/IDLE/NO_SWORD/3.png'),
	],
	'idle_sword': [
		os.path.join(BASE_DIR, 'assets/PLAYER/IDLE/WITH_SWORD/38.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/IDLE/WITH_SWORD/39.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/IDLE/WITH_SWORD/40.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/IDLE/WITH_SWORD/41.png'),
	],
	'jump': [
		os.path.join(BASE_DIR, 'assets/PLAYER/JUMP/1.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/JUMP/2.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/JUMP/3.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/JUMP/4.png'),
	],
	'jump_flip': [
		os.path.join(BASE_DIR, 'assets/PLAYER/JUMP_FLIP/16.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/JUMP_FLIP/17.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/JUMP_FLIP/18.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/JUMP_FLIP/19.png'),
	],
	'run': [
		os.path.join(BASE_DIR, 'assets/PLAYER/RUN/4.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/RUN/5.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/RUN/6.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/RUN/7.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/RUN/8.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/RUN/9.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/RUN/10.png'),
	],
	'slide': [
		os.path.join(BASE_DIR, 'assets/PLAYER/SLIDE/23.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/SLIDE/24.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/SLIDE/25.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/SLIDE/26.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/SLIDE/27.png'),
	],
	'attack_1': [
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/ATTACK_1/1.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/ATTACK_1/2.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/ATTACK_1/3.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/ATTACK_1/4.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/ATTACK_1/5.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/ATTACK_1/6.png'),
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
		os.path.join(BASE_DIR, 'assets/PLAYER/FALL/21.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/FALL/22.png'),
	],
	'hurt': [
		os.path.join(BASE_DIR, 'assets/PLAYER/HURT/0.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/HURT/1.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/HURT/2.png'),
	],
	'crouch': [
		os.path.join(BASE_DIR, 'assets/PLAYER/CROUCH/4.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/CROUCH/5.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/CROUCH/6.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/CROUCH/13.png'),
	],
	'die': [
		os.path.join(BASE_DIR, 'assets/PLAYER/DIE/die_1.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/DIE/die_2.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/DIE/die_3.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/DIE/die_4.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/DIE/die_5.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/DIE/die_6.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/DIE/die_7.png'),
	],
	'draw_sword': [
		os.path.join(BASE_DIR, 'assets/PLAYER/SWORD/DRAW_SWORD/draw_sword_1.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/SWORD/DRAW_SWORD/draw_sword_2.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/SWORD/DRAW_SWORD/draw_sword_3.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/SWORD/DRAW_SWORD/draw_sword_4.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/SWORD/DRAW_SWORD/draw_sword_5.png'),
	],
	'put_back': [
		os.path.join(BASE_DIR, 'assets/PLAYER/SWORD/PUT_BACK/put_back_1.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/SWORD/PUT_BACK/put_back_2.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/SWORD/PUT_BACK/put_back_3.png'),
	],
	'shoot_stand': [
		os.path.join(BASE_DIR, 'assets/PLAYER/BOW/SHOOT_STAND/1.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/BOW/SHOOT_STAND/2.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/BOW/SHOOT_STAND/3.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/BOW/SHOOT_STAND/4.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/BOW/SHOOT_STAND/5.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/BOW/SHOOT_STAND/6.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/BOW/SHOOT_STAND/7.png'),
	],
	'release_bow': [
		os.path.join(BASE_DIR, 'assets/PLAYER/BOW/RELEASE/8.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/BOW/RELEASE/9.png'),
	],
	'hold_bow': [
		os.path.join(BASE_DIR, 'assets/PLAYER/BOW/SHOOT_STAND/7.png'),
	],
	'punch_1': [
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/PUNCH_1/0.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/PUNCH_1/1.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/PUNCH_1/2.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/PUNCH_1/3.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/PUNCH_1/4.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/PUNCH_1/5.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/PUNCH_1/6.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/PUNCH_1/7.png'),
	],
	'punch_2': [
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/PUNCH_1/0.png'),
	],
	'top_down': [
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/TOP_DOWN/0.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/TOP_DOWN/1.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/TOP_DOWN/2.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/TOP_DOWN/3.png'),
	]
}
