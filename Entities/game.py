from Entities import player, deck, card, lane

class Game(object):

    def __init__(self, handsize) -> None:
        self.p1 = player.Player(id=0)
        self.p2 = player.Player(id=1)
        self.l1 = lane.Lane(id=1)
        self.l2 = lane.Lane(id=2)
        self.l3 = lane.Lane(id=3)
        self.lane_list = [self.l1, self.l2, self.l3]
        self.deck = deck.Deck()
        self.handsize = handsize

    def setup(self):
        self.deck.generate()
        self.deck.shuffle()
        self.deck.deal_basecards(self.lane_list)
        self.deck.deal_hand(self.p1, self.p2, self.handsize)

    def display_board(self):
        for lane in self.lane_list:
            lane.display()
        
    def run_game(self):

