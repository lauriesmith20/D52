from Entities.card import BaseCard
from CustomErrors.CustomErrors import CardAlreadyFlippedError

class Ace(BaseCard):
    def __init__(self, suit):
        self.value = 'A'
        super().__init__(suit)
    
    def flip(self, game, lane, player):
        if self.flipped:
            raise CardAlreadyFlippedError(self)
        
        self.flipped = True
        print('ACE EXTRA GO')
        game.moves_remaining += 1