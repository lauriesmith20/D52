from Entities.card import BaseCard

class Queen(BaseCard):
    def __init__(self, suit):
        self.value = 'Q'
        super().__init__(suit)
    