from Lane import BaseLane

class Player(object):

    def __init__(self, id) -> None:
        self.id = id
        self.lane_one = BaseLane()
        self.lane_two = BaseLane()
        self.lane_three = BaseLane()
        self.hand = []
        