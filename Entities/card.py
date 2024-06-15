from CustomErrors import CustomErrors as E

class BaseCard(object):

    def __init__(self, suit):
        self.suit = suit
        self.health = self.max_health = 2
        self.flipped = False
        self.value = None if not self.value else self.value

    def flip(self, game, lane, player):
        if not self.flipped:
            self.flipped = True
        else:
            raise E.CardAlreadyFlippedError(self)


    def attack(self, lane, enemy):
        if self.flipped:
            result = enemy.get_attacked(lane, self)
        else:
            raise E.UnflippedCardAttackError(self)

        return result

    def get_attacked(self, lane, attacker):
        self.health -= 1
        
        if self.health > 0:
            result = 'Damaged'
        if self.health == 0:
            result = 'Killed'
            self.die(lane)
        
        return result

    def die(self, lane):
        for cardlist in lane.cards:
            if self in cardlist:
                cardlist.remove(self)
        return
    
    def get_display_string(self, display_hand = False):

        return f'{self.value}{self.suit}{self.health}' if (self.flipped or display_hand) else f'xx{self.health}'
