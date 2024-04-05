class Player(object):

    def __init__(self, id) -> None:
        self.id = id
        self.hand = []
    
    def display_hand(self):
        disp = ''

        for card in self.hand:
            disp += f'{card.get_display_string(display_hand = True)} '
        
        print(disp)