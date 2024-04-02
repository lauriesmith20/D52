from Entities.Card import BaseCard

class Six(BaseCard):
    def __init__(self, suit):
        self.value = '6'
        super().__init__(suit)