from Entities.Cards import ace, two, three, four, five, six, seven, eight, nine, ten, jack, queen, king
from random import shuffle

class Deck(object):

    def __init__(self) -> None:
        self.cards = []
        self.all_cards = []

    def generate(self):
        suits = ['H', 'D', 'S', 'C']
        values = [ace.Ace, two.Two, three.Three, four.Four, five.Five, six.Six, seven.Seven, eight.Eight, nine.Nine, ten.Ten, jack.Jack, queen.Queen, king.King]

        for s in suits:
            for v in values:
                new_card = v(s)
                self.cards.append(new_card)
                self.all_cards.append(new_card)
    
    def shuffle(self):
        shuffle(self.cards)

    def display(self):
        display_list = [c.value+c.suit for c in self.cards]
        print(display_list)

    def deal_basecards(self, lane_list):
        
        for l in lane_list:
            p1_card = self.cards.pop()
            p2_card = self.cards.pop()
            l.accept_basecards(p1_card, p2_card)

    def deal_hand(self, p1, p2, handsize):

        for i in range(handsize):
            p1_card = self.cards.pop()
            p2_card = self.cards.pop()
            p1.hand.append(p1_card)
            p2.hand.append(p2_card)
    
    def burn_cards(self, count):

        for i in range(count):
            self.cards.pop()
