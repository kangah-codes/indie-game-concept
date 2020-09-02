from MAIN.game_manager import *
from PLAYER.sprite import *

testGame = GameManager()

player = Player()

testGame.player = player
testGame.mainLoop()

