from Entities import player, deck, card, lane

class Game(object):

    def __init__(self, handsize, no_to_burn, display=True) -> None:
        self.display = display

        self.p1 = player.Player(id=0, name = 'Laurie', display=display)
        self.p2 = player.Player(id=1, name = 'Bot', display=display)
        self.l1 = lane.Lane(id=1)
        self.l2 = lane.Lane(id=2)
        self.l3 = lane.Lane(id=3)
        self.lane_list = [self.l1, self.l2, self.l3]
        self.deck = deck.Deck()
        self.active_player = self.p1 
        self.inactive_player = self.p2
        self.moves_remaining = 2

        self.handsize = handsize
        self.no_to_burn = no_to_burn
        self.endgame = False
        self.game_over = False
    def setup(self):
        self.deck.generate()
        self.deck.shuffle()
        self.deck.deal_basecards(self.lane_list)
        self.deck.deal_hand(self.p1, self.p2, self.handsize)
        self.deck.burn_cards(self.no_to_burn)
        self.first_turn = True

    def display_board(self):
        if not self.display:
            return
        
        for lane in self.lane_list:
            lane.display()
        
    def run_game(self):

        while not self.game_over:

            self.begin_turn()

            while self.moves_remaining > 0:
                self.use_move()
                self.check_game_status()
                
            self.end_turn()
        
        return self.winner

    def use_move(self):
        legal_moves = self.active_player.gather_legal_moves(self.lane_list)
        move_type, move_params = self.active_player.select_random_move(legal_moves)

        if move_type and move_params:
            self.active_player.make_move(self, move_type, *move_params)
            self.moves_remaining -= 1
        else:
            self.moves_remaining = 0

    def begin_turn(self):

        if not self.endgame:
            self.active_player.pickup_card(self.deck)

        if not self.deck.cards and not self.endgame:
            self.begin_endgame()

    def end_turn(self):

        if self.game_over:
            self.end_game()
            return

        self.moves_remaining = 3 
        self.display_board()
        self.switch_player()
        if self.display:
            print('================================================================')

    def switch_player(self):
        old_active = self.active_player
        self.active_player = self.inactive_player
        self.inactive_player = old_active


    def begin_endgame(self):

        self.endgame = True

        for lane in self.lane_list:
            lane.activate_basecards()

    def check_game_status(self):

        if not self.endgame:
            return

        for lane in self.lane_list:
            if lane.won:
                continue

            elif len(lane.cards[self.inactive_player.id]) == 0:
                lane.won = True
                lane.winner = self.active_player.id
                self.active_player.lanes_won += 1
            
            elif len(lane.cards[self.active_player.id]) == 0:
                lane.won = True
                lane.winner = self.inactive_player.id
                self.inactive_player.lanes_won += 1
            
        if self.active_player.lanes_won == 2:
            self.game_over = True
            self.moves_remaining = 0
            self.winner = self.active_player
        
        elif self.inactive_player.lanes_won == 2:
            self.game_over = True
            self.moves_remaining = 0
            self.winner = self.inactive_player
            print(f'ULTRA RARE WIN')
            raise IndexError
    
    def end_game(self):
        self.display_board()
        print(f'GAME OVER! {self.winner.name} wins')


            
        



