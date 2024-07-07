from Entities.card import BaseCard
from CustomErrors.CustomErrors import CardAlreadyFlippedError

class Jack(BaseCard):
    def __init__(self, suit):
        self.value = 'J'
        super().__init__(suit)
    
    def flip(self, game, lane, player):
        if self.flipped:
            raise CardAlreadyFlippedError(self)
        
        self.flipped = True
        self.health += 1
        self.max_health = 3
    
    def get_attacked(self, lane, attacker, by_eight=False):

        if attacker.value == '9':
            self.health -= 2
        else:
            self.health -= 1
        
        if self.health > 0:
            result = 'Damaged'
        if self.health <= 0:
            result = 'Killed'
            self.die(lane)
        
        return result
        