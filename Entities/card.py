from CustomErrors import CustomErrors as E

class BaseCard(object):

    def __init__(self, suit):
        self.suit = suit
        self.health = 2
        self.flipped = False

    def flip(self):
        if not self.flipped:
            self.flipped = True
        else:
            raise E.CardAlreadyFlipped(self)


    def attack(self, defender):
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
    
    def get_display_string(self, display_hand = False):

        return self.value + self.suit if (self.flipped or display_hand) else 'xx'
