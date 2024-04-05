from Entities.card import BaseCard

class Nine(BaseCard):
    def __init__(self, suit):
        self.value = '9'
        super().__init__(suit)