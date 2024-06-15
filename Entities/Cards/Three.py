from Entities.card import BaseCard

class Three(BaseCard):
    def __init__(self, suit):
        self.value = '3'
        super().__init__(suit)
    
    def die(self, lane):
        if not self.flipped:
            print('3 SELF REVIVES')
            self.flipped = True
            self.health = 2
            return
        
        for cardlist in lane.cards:
            if self in cardlist:
                cardlist.remove(self)
        
        
        