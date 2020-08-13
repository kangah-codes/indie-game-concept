from MAIN.dev_game import *
from PLAYER.sprite import *

testGame = Game()
player = Player()

testGame.player = player
testGame.mainLoop()