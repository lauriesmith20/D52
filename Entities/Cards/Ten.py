from Entities.card import BaseCard
import CustomErrors.CustomErrors as E

class Ten(BaseCard):
    def __init__(self, suit):
        self.value = '10'
        super().__init__(suit)
    
    def attack(self, lane, enemy, by_eight=False):
        self.no_of_attacks -= 1

        if self.flipped:
            result = enemy.get_attacked(lane, self, by_eight)
        else:
            raise E.UnflippedCardAttackError(self)

        return result