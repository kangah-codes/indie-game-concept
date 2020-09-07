from MAIN.game_manager import *
from PLAYER.sprite import *
from ENEMIES.BAT.bat import *

testGame = GameManager()

player = Player()
testGame.enemyEntities.append(Bat('idle', 'bat', 100, 50))
testGame.player = player
testGame.mainLoop()
