from Entities.card import BaseCard

class Seven(BaseCard):
    def __init__(self, suit):
        self.value = '7'
        super().__init__(suit)
    
    def flip(self, lane, player):

        self.flipped = True
        print('7 HEALS ALL')
        for card in lane.cards[player]:
            card.health = card.max_health
