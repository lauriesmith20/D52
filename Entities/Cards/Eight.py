from Entities.card import BaseCard

class Eight(BaseCard):
    def __init__(self, suit):
        self.value = '8'
        super().__init__(suit)
    
    def get_attacked(self, lane, attacker, by_eight=False):
        self.health -= 1
        
        if self.flipped and not by_eight and attacker.value != '9':
            self.attack(lane, attacker, by_eight=True)

        if self.health > 0:
            result = 'Damaged'
        if self.health == 0:
            result = 'Killed'
            self.die(lane)
        
        return result
    