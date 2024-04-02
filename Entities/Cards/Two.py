from Entities.Card import BaseCard

class Two(BaseCard):
    def __init__(self, suit):
        self.value = '2'
        super().__init__(suit)
        