import random

class Player(object):

    def __init__(self, id) -> None:
        self.id = id
        self.hand = []
    
    def pickup_card(self, deck):
        top_card = deck.cards.pop()
        self.hand.append(top_card)

    def display_hand(self):
        disp = ''

        for card in self.hand:
            disp += f'{card.get_display_string(display_hand = True)} '
        
        print(disp)

    def gather_legal_moves(self, lane_list):
        legal_moves = {     'place' : []
                       ,    'flip' : []
                       ,    'attack' : []
                       }

        for lane in lane_list:

            for card in self.hand:
                legal_moves['place'].append((card, lane))
            
            for card in lane.cards[self.id]:
                
                if not card.flipped():
                    legal_moves['flip'].append((card, lane))
                
        return legal_moves
    

    def select_random_move(self, legal_moves):

        move_type, move_list = random.choice(list(legal_moves.items()))

        while not move_list:
            move_type, move_list = random.choice(list(legal_moves.items()))
        
        move_params = random.choice(move_list)

        return move_type, move_params


    def make_move(self, move_type, card, lane, enemy = None):

        if move_type == 'place':
            print('place')
        
        elif move_type == 'flip':
            print('flip')
        
        elif move_type == 'attack':
            print('attack')

    