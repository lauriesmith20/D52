from Entities.card import BaseCard
from CustomErrors.CustomErrors import CardAlreadyFlippedError

class Seven(BaseCard):
    def __init__(self, suit):
        self.value = '7'
        super().__init__(suit)
    
    def flip(self, game, lane, player):

        if self.flipped:
            raise CardAlreadyFlippedError(self)
        
        self.flipped = True
        print('7 HEALS ALL')
        for card in lane.cards[player.id]:
            card.health = card.max_health
