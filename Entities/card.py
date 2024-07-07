from CustomErrors import CustomErrors as E

class BaseCard(object):

    def __init__(self, suit):
        self.suit = suit
        self.health = self.max_health = 2
        self.flipped = False
        self.value = None if not self.value else self.value

        self.no_of_attacks = 1
        self.frozen = False

    def flip(self, game, lane, player):
        if not self.flipped:
            self.flipped = True
        else:
            raise E.CardAlreadyFlippedError(self)

        self.activate_power(game, lane, player)


    def attack(self, lane, enemy, by_eight=False):
        self.no_of_attacks -= 1

        if self.flipped:
            result = enemy.get_attacked(lane, self, by_eight)
        else:
            raise E.UnflippedCardAttackError(self)

        return result

    def get_attacked(self, lane, attacker, by_eight=False):
        self.health -= 1

        if self.health > 0:
            result = 'Damaged'
        if self.health == 0:
            result = 'Killed'
            self.die(lane)
        if self.value == '10' and self.health < 0:
            result = None
            self.die(lane)
        
        return result

    def die(self, lane):
        for cardlist in lane.cards:
            if self in cardlist:
                cardlist.remove(self)
        return

    def activate_power(self, game, lane, player):
        pass
    
    def get_display_string(self, display_hand = False):

        return f'{self.value}{self.suit}{self.health}' if (self.flipped or display_hand) else f'xx{self.health}'
