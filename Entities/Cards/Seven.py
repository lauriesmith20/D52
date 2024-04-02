from Entities.Card import BaseCard

class Seven(BaseCard):
    def __init__(self, suit):
        self.value = '7'
        super().__init__(suit)