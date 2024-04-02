from Entities.Card import BaseCard

class Three(BaseCard):
    def __init__(self, suit):
        self.value = '3'
        super().__init__(suit)