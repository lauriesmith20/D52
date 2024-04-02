from Entities.Cards import ace, two, three, four, five, six, seven, eight, nine, ten, jack, queen, king
from random import shuffle

class DeckClass(object):

    def __init__(self) -> None:
        self.cards = []

    def generate(self):
        suits = ['H', 'D', 'S', 'C']
        values = [ace.Ace, two.Two, three.Three, four.Four, five.Five, six.Six, seven.Seven, eight.Eight, nine.Nine, ten.Ten, jack.Jack, queen.Queen, king.King]

        for s in suits:
            for v in values:
                new_card = v(s)
                self.cards.append(new_card)
    
    def shuffle(self):
        shuffle(self.cards)

    def display(self):
        display_list = [c.value+c.suit for c in self.cards]
        print(display_list)
