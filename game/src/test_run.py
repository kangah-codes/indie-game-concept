from MAIN.game_manager import *
from PLAYER.sprite import *
from ENEMIES.bat import *
from ENEMIES.tree import *
from ENEMIES.eye import *
from ENEMIES.goblin import *
from ENEMIES.mushroom import *
from ENEMIES.skeleton import *

testGame = GameManager()

player = Player()
testGame.enemyEntities.add(Skeleton('idle', 'skeleton', 100, 50))
# testGame.enemyEntities.add(Eye('idle', 'eye', 100, 50))
# testGame.enemyEntities.add(Bat('idle', 'bat', 100, 50))
# testGame.enemyEntities.add(Tree('idle', 'tree', 100, 50))
testGame.player = player
testGame.mainLoop()
