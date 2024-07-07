from Entities.card import BaseCard

class Two(BaseCard):
    def __init__(self, suit):
        self.value = '2'
        super().__init__(suit)
    
    def activate_power(self, game, lane, player):
        if not game.endgame:
            player.pickup_card(game.deck)
            player.discard_one()
        