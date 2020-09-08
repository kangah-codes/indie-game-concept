from MAIN.game_manager import *
from PLAYER.sprite import *
from ENEMIES.BAT.bat import *
from ENEMIES.TREE.tree import *

testGame = GameManager()

player = Player()
testGame.enemyEntities.add(Tree('idle', 'tree', 100, 50))
testGame.player = player
testGame.mainLoop()
