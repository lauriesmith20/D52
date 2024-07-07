from Entities.card import BaseCard

class Queen(BaseCard):
    def __init__(self, suit):
        self.value = 'Q'
        super().__init__(suit)
    
    def activate_power(self, game, lane, player):

        card_moves = [(None, None)]

        for l in game.lane_list:
            if l != lane:
                for card in l.cards[player.id]:
                    card_moves.append((card, l))
        
        player.select_card_move(player, card_moves, lane)
    