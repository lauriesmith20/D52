from Entities.Card import BaseCard

class Ace(BaseCard):
    def __init__(self, suit):
        self.value = 'A'
        super().__init__(suit)