class Lane(object):

    def __init__(self, id) -> None:
        self.id = id
        self.basecards = [[],[]]
        self.cards = [[],[]]

    def accept_basecards(self, p1_card, p2_card):

        self.basecards[0].append(p1_card)
        self.basecards[1].append(p2_card)

    def display(self):
        disp = ''
        sections = [self.basecards[0], self.cards[0], self.cards[1], self.basecards[1]]
        seps = ['|', ':', '|', ':']
        
        for i, sec in enumerate(sections):
            disp += seps[i]
            for card in sec:
                disp += f' {card.get_display_string()} '

        disp += '|'
        print(disp)