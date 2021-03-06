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
	'sprint_slow': [
		os.path.join(BASE_DIR, 'assets/PLAYER/RUN/RUN_1/run_1.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/RUN/RUN_1/run_2.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/RUN/RUN_1/run_3.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/RUN/RUN_1/run_4.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/RUN/RUN_1/run_5.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/RUN/RUN_1/run_6.png'),
	],
	'sprint_fast':[
		os.path.join(BASE_DIR, 'assets/PLAYER/RUN/RUN_2/adventurer-run2-00.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/RUN/RUN_2/adventurer-run2-01.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/RUN/RUN_2/adventurer-run2-02.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/RUN/RUN_2/adventurer-run2-03.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/RUN/RUN_2/adventurer-run2-04.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/RUN/RUN_2/adventurer-run2-05.png'),
	],
	'sprint_sword': [
		os.path.join(BASE_DIR, 'assets/PLAYER/RUN/RUN_SWORD/adventurer-run3-00.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/RUN/RUN_SWORD/adventurer-run3-01.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/RUN/RUN_SWORD/adventurer-run3-02.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/RUN/RUN_SWORD/adventurer-run3-03.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/RUN/RUN_SWORD/adventurer-run3-04.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/RUN/RUN_SWORD/adventurer-run3-05.png'),
	],
	'walk': [
		os.path.join(BASE_DIR, 'assets/PLAYER/RUN/WALK/adventurer-walk-00.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/RUN/WALK/adventurer-walk-01.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/RUN/WALK/adventurer-walk-02.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/RUN/WALK/adventurer-walk-03.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/RUN/WALK/adventurer-walk-04.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/RUN/WALK/adventurer-walk-05.png'),
	],
	'slide': [
		os.path.join(BASE_DIR, 'assets/PLAYER/SLIDE/slide_1.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/SLIDE/slide_2.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/SLIDE/slide_3.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/SLIDE/slide_4.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/SLIDE/slide_5.png'),
	],
	'sword_attack_1': [
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/ATTACK_1/attack_1_1.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/ATTACK_1/attack_1_2.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/ATTACK_1/attack_1_3.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/ATTACK_1/attack_1_4.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/ATTACK_1/attack_1_5.png'),
	],
	'sword_attack_2': [
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/ATTACK_2/attack_2_1.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/ATTACK_2/attack_2_2.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/ATTACK_2/attack_2_3.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/ATTACK_2/attack_2_4.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/ATTACK_2/attack_2_5.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/ATTACK_2/attack_2_6.png'),
	],
	'sword_attack_3': [
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/ATTACK_3/attack_3_1.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/ATTACK_3/attack_3_2.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/ATTACK_3/attack_3_3.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/ATTACK_3/attack_3_4.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/ATTACK_3/attack_3_5.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/ATTACK_3/attack_3_6.png'),
	],
	'cast_spell': [
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/CAST_SPELL/adventurer-cast-00.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/CAST_SPELL/adventurer-cast-01.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/CAST_SPELL/adventurer-cast-02.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/CAST_SPELL/adventurer-cast-03.png'),
	],
	'cast_spell_loop': [
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/CAST_SPELL_LOOP/adventurer-cast-loop-00.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/CAST_SPELL_LOOP/adventurer-cast-loop-01.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/CAST_SPELL_LOOP/adventurer-cast-loop-02.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/CAST_SPELL_LOOP/adventurer-cast-loop-03.png'),
	],
	'shoot_bow_standing': [
		os.path.join(BASE_DIR, 'assets/PLAYER/BOW/SHOOT_STAND/1.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/BOW/SHOOT_STAND/2.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/BOW/SHOOT_STAND/3.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/BOW/SHOOT_STAND/4.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/BOW/SHOOT_STAND/5.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/BOW/SHOOT_STAND/6.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/BOW/SHOOT_STAND/7.png'),
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
		os.path.join(BASE_DIR, 'assets/PLAYER/CROUCH/CROUCH/crouch1.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/CROUCH/CROUCH/crouch2.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/CROUCH/CROUCH/crouch3.png'),
	],
	'crouch_walk': [
		os.path.join(BASE_DIR, 'assets/PLAYER/CROUCH/CROUCH_WALK/adventurer-crouch-walk-00.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/CROUCH/CROUCH_WALK/adventurer-crouch-walk-01.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/CROUCH/CROUCH_WALK/adventurer-crouch-walk-02.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/CROUCH/CROUCH_WALK/adventurer-crouch-walk-03.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/CROUCH/CROUCH_WALK/adventurer-crouch-walk-04.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/CROUCH/CROUCH_WALK/adventurer-crouch-walk-05.png'),
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
	'release_bow': [
		os.path.join(BASE_DIR, 'assets/PLAYER/BOW/RELEASE/8.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/BOW/RELEASE/9.png'),
	],
	'release_bow_jumping': [
		os.path.join(BASE_DIR, 'assets/PLAYER/BOW/RELEASE_JUMP/5.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/BOW/RELEASE_JUMP/6.png'),
	],
	'hold_bow': [
		os.path.join(BASE_DIR, 'assets/PLAYER/BOW/SHOOT_STAND/7.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/BOW/SHOOT_STAND/6.png'),
	],
	'hold_bow_jumping': [
		os.path.join(BASE_DIR, 'assets/PLAYER/BOW/HOLD_JUMPING/3.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/BOW/HOLD_JUMPING/4.png'),
	],
	'stretch_bow_jumping': [
		os.path.join(BASE_DIR, 'assets/PLAYER/BOW/SHOOT_JUMP/1.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/BOW/SHOOT_JUMP/2.png'),
	],
	'knock_down': [
		os.path.join(BASE_DIR, 'assets/PLAYER/KNOCK_DOWN/adventurer-knock-dwn-00.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/KNOCK_DOWN/adventurer-knock-dwn-01.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/KNOCK_DOWN/adventurer-knock-dwn-02.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/KNOCK_DOWN/adventurer-knock-dwn-03.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/KNOCK_DOWN/adventurer-knock-dwn-04.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/KNOCK_DOWN/adventurer-knock-dwn-05.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/KNOCK_DOWN/adventurer-knock-dwn-06.png'),
	],
	'get_up': [
		os.path.join(BASE_DIR, 'assets/PLAYER/GET_UP/adventurer-get-up-00.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/GET_UP/adventurer-get-up-01.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/GET_UP/adventurer-get-up-02.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/GET_UP/adventurer-get-up-03.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/GET_UP/adventurer-get-up-04.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/GET_UP/adventurer-get-up-05.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/GET_UP/adventurer-get-up-06.png'),
	],
	'kick': [
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/KICK/adventurer-kick-00.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/KICK/adventurer-kick-01.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/KICK/adventurer-kick-02.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/KICK/adventurer-kick-03.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/KICK/adventurer-kick-04.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/KICK/adventurer-kick-05.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/KICK/adventurer-kick-06.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/KICK/adventurer-kick-07.png'),
	],
	'punch_1': [
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/PUNCH_1/adventurer-punch-00.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/PUNCH_1/adventurer-punch-04.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/PUNCH_1/adventurer-punch-05.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/PUNCH_1/adventurer-punch-06.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/PUNCH_1/adventurer-punch-07.png'),
	],
	'punch_2': [
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/PUNCH_2/adventurer-punch-08.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/PUNCH_2/adventurer-punch-09.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/PUNCH_2/adventurer-punch-10.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/PUNCH_2/adventurer-punch-11.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/PUNCH_2/adventurer-punch-12.png'),
	],
	'punch_3': [
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/PUNCH_3/adventurer-run-punch-00.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/PUNCH_3/adventurer-run-punch-01.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/PUNCH_3/adventurer-run-punch-02.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/PUNCH_3/adventurer-run-punch-03.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/PUNCH_3/adventurer-run-punch-04.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/PUNCH_3/adventurer-run-punch-05.png'),
		os.path.join(BASE_DIR, 'assets/PLAYER/ATTACK/PUNCH_3/adventurer-run-punch-06.png'),
	]
}
