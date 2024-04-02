import CustomErrors as E

class BaseCardEntity(object):

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.health = 2
        self.flipped = False

    def flip(self):
        if not self.flipped:
            self.flipped = True
        else:
            raise E.CardAlreadyFlipped(self)


    def attack(self, defender: BaseCardEntity):
        if self.flipped:
            defender.get_attacked(self)
        else:
            raise E.UnflippedCardAttack(self)

    def get_attacked(self, attacker):
        self.health -= 1
        
        if self.health == 1:
            pass
        if self.health == 0:
            self.die()
        
        return

    def die(self):
        pass
        return
    
