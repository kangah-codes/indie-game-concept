from PLAYER.physics import *
from CONFIG.game import *
from PLAYER.sprite import *


game = Game()

game.spriteGroup.add(Player(game.space))

game.run()

# p = Player(game.space)