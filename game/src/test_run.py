from CONFIG.game import *
from PLAYER.sprite import *


game = Game()

p = Player()

game.playerGroup.append(p)

game.run()

# p = Player(game.space)