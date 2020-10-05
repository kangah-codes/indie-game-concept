from MAIN.game_manager import *
from PLAYER.sprite import *
from ENEMIES.bat import *
from ENEMIES.tree import *
from ENEMIES.eye import *
from ENEMIES.goblin import *
from ENEMIES.mushroom import *
from ENEMIES.skeleton import *
from ENEMIES.slime import *

testGame = GameManager()

testGame.enemyEntities.add(Slime('idle', 'slime', 10, 50))
testGame.enemyEntities.add(Eye('idle', 'eye', 30, 50))
testGame.enemyEntities.add(Bat('idle', 'bat', 50, 50))
testGame.enemyEntities.add(Tree('idle', 'tree', 70, 50))
testGame.enemyEntities.add(Goblin('idle', 'goblin', 90, 50))
testGame.enemyEntities.add(Skeleton('idle', 'skeleton', 110, 50))
testGame.player = Player()
testGame.mainLoop()
