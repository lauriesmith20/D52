from Entities.card import BaseCard

class Jack(BaseCard):
    def __init__(self, suit):
        self.value = 'J'
        super().__init__(suit)