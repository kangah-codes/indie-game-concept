"""
	Module for handling loading of player sprites
	author: Joshua Akangah
    date: 10/9/20
"""

from .settings import *

"""
	Using a dictionary to store player states
	It is easier this way since we can quickly switch through player states using strings as keys
"""
player_states = {
	'idle': [],
	'jump': [],
	'jump_flip': [],
	'run': [],
	'slide': [],
	'holding_sword': [],
	'attack_1': [],
	'attack_2': [],
	'attack_3': [],
	'shoot_bow_standing': [],
	'shoot_bow_jumping': [],
	'climb': [],
	'fall': [],
	'hurt': [],
	'crouch': [],
	'die': []
}