from Entities.card import BaseCard
from CustomErrors.CustomErrors import CardAlreadyFlippedError

class King(BaseCard):
    def __init__(self, suit):
        self.value = 'K'
        super().__init__(suit)
    
    def activate_power(self, game, lane, player):
        #print('K ACTIVATES ALL')
        cards_to_activate = [c for c in lane.cards[player.id] if (c.flipped and c.value !='K')]
        for card in cards_to_activate:
            if card.value != 'K' and card.flipped:
                card.activate_power(game, lane, player)