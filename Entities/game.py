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
        self.active_player = self.p1 
        self.moves_remaining = 2

        self.handsize = handsize
        self.game_over = False

    def setup(self):
        self.deck.generate()
        self.deck.shuffle()
        self.deck.deal_basecards(self.lane_list)
        self.deck.deal_hand(self.p1, self.p2, self.handsize)
        self.first_turn = True

    def display_board(self):
        for lane in self.lane_list:
            lane.display()
        
    def run_game(self):

        while not self.game_over:

            self.begin_turn()

            while self.moves_remaining > 0: 
                legal_moves = self.active_player.gather_legal_moves(self.lane_list)
                move_type, move_params = self.active_player.select_random_move(legal_moves)
                self.active_player.make_move(move_type, *move_params)

                self.moves_remaining -= 1

            self.end_turn()

    def begin_turn(self):

        self.active_player.pickup_card(self.deck)

    def end_turn(self):

        self.moves_remaining = 3 
        self.game_over = True



