from Entities.card import BaseCard
from CustomErrors.CustomErrors import CardAlreadyFlippedError

class Five(BaseCard):
    def __init__(self, suit):
        self.value = '5'
        super().__init__(suit)
        
    def activate_power(self, game, lane, player):
        print('5 FLIPS ALL')
        for card in lane.cards[player.id]:
            try:
                card.flip(game, lane, player)
            except CardAlreadyFlippedError:
                continue