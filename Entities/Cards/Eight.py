from Entities.card import BaseCard

class Eight(BaseCard):
    def __init__(self, suit):
        self.value = '8'
        super().__init__(suit)