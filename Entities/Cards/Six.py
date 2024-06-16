from Entities.card import BaseCard
from CustomErrors.CustomErrors import CardAlreadyFlippedError

class Six(BaseCard):
    def __init__(self, suit):
        self.value = '6'
        super().__init__(suit)
    

    def activate_power(self, game, lane, player):

        for card in lane.cards[abs(player.id-1)]:
            if card.value != '9':
                card.frozen = True