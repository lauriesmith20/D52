from Entities.Card import BaseCard

class Ten(BaseCard):
    def __init__(self, suit):
        self.value = '10'
        super().__init__(suit)