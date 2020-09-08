from MAIN.game_manager import *
from PLAYER.sprite import *
from ENEMIES.BAT.bat import *
from ENEMIES.TREE.tree import *
from ENEMIES.EYE.eye import *
from ENEMIES.GOBLIN.goblin import *

testGame = GameManager()

player = Player()
testGame.enemyEntities.add(Goblin('idle', 'goblin', 100, 50))
testGame.enemyEntities.add(Eye('idle', 'eye', 100, 50))
testGame.enemyEntities.add(Bat('idle', 'bat', 100, 50))
testGame.enemyEntities.add(Tree('idle', 'tree', 100, 50))
testGame.player = player
testGame.mainLoop()
