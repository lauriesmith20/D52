from Entities.card import BaseCard
from CustomErrors.CustomErrors import CardAlreadyFlippedError

class Ace(BaseCard):
    def __init__(self, suit):
        self.value = 'A'
        super().__init__(suit)
        
    def activate_power(self, game, lane, player):
        #print('ACE EXTRA GO')
        game.moves_remaining += 1
        self.no_of_attacks += 1