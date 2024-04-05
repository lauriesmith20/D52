from Entities.card import BaseCard

class King(BaseCard):
    def __init__(self, suit):
        self.value = 'K'
        super().__init__(suit)