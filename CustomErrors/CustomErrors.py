class UnflippedCardAttackError(Exception):

    def __init__(self, card) -> None:
        self.message = f"A card ({card.value}{card.suit}) attempted to make an attack while flipped = {card.flipped}. A card must be flipped to attack."
        super().__init__(self.message)


class CardAlreadyFlippedError(Exception):

    def __init__(self, card) -> None:
        self.message = f"An attempt was made to flip a card with flipped = {card.flipped}. Only unflipped cards may be flipped."
        super().__init__(self.message)

