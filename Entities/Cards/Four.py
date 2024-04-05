from Entities.card import BaseCard

class Four(BaseCard):
    def __init__(self, suit):
        self.value = '4'
        super().__init__(suit)