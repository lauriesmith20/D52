import random


class Player(object):

    def __init__(self, id, name, display=True) -> None:
        self.name = name
        self.id = id  # Either 0 or 1
        self.hand = []
        self.lanes_won = 0
        self.display = display

    def pickup_card(self, deck):
        top_card = deck.cards.pop()
        self.hand.append(top_card)

    def display_hand(self):
        disp = ""

        for card in self.hand:
            disp += f"{card.get_display_string(display_hand = True)} "

        self.display_message(disp)

    def gather_legal_moves(self, lane_list):
        legal_moves = {"place": [], "flip": [], "attack": []}

        for lane in lane_list:

            for card in self.hand:
                legal_moves["place"].append((card, lane))

            for card in lane.cards[self.id]:

                if not card.flipped and not card.frozen:
                    legal_moves["flip"].append((card, lane))

                if card.flipped and card.no_of_attacks > 0 and not card.frozen:
                    for enemy in lane.cards[abs(self.id - 1)]:
                        legal_moves["attack"].append((card, lane, enemy))

        return legal_moves

    def select_random_move(self, legal_moves):

        if not any(legal_moves.values()):
            self.display_message("No remaining legal moves")
            return None, None

        possible_moves = ["place", "flip", "attack"]
        random.shuffle(possible_moves)
        move_list = None

        while not move_list:
            move_type = possible_moves.pop()
            move_list = legal_moves[move_type]

        move_params = random.choice(move_list)

        return move_type, move_params

    def make_move(self, game, move_type, card, lane=None, enemy=None):

        if move_type == "place":
            self.place_card(card, lane)

        elif move_type == "flip":
            self.flip_card(game, card, lane)

        elif move_type == "attack":
            self.attack(card, lane, enemy)

    def place_card(self, card, lane):

        self.hand.remove(card)
        lane.cards[self.id].append(card)

        self.display_message(f"{self.name} placed a card in lane {lane.id}")

    def flip_card(self, game, card, lane):

        card.flip(game, lane, self)

        self.display_message(f"{self.name} flipped a {card.get_display_string()} in lane {lane.id}")

    def attack(self, card, lane, enemy):
        
        result = card.attack(lane, enemy)
        self.display_message(
            f"""{self.name} {result} a {enemy.get_display_string()} in lane {lane.id} using {card.get_display_string()}"""
        )
    
    def discard_one(self):
        card = self.hand.pop(random.randint(0, len(self.hand)-1))
        print(f'{self.name} discarded a card ({card.value})')
    
    def select_card_move(self, player, moves, to_lane):
        card, from_lane = random.choice(moves)
        if not card and not from_lane:
            print('NO 3 MOVE CHOSEN')
            return
        
        from_lane.display()
        to_lane.display()
        print(f'Moving {card.value + card.suit} from {from_lane.id} to {to_lane.id}')
        from_lane.cards[player.id].remove(card)
        to_lane.cards[player.id].append(card)
        from_lane.display()
        to_lane.display()

    def display_message(self, message):
        if self.display:
            print(message)

