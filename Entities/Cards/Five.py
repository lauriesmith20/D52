from Entities.card import BaseCard

class Five(BaseCard):
    def __init__(self, suit):
        self.value = '5'
        super().__init__(suit)