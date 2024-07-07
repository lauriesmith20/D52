from Entities import game

wins = [0, 0]
for i in range(100):
    g = game.Game(handsize = 5, no_to_burn = 10, display = False)
    g.setup()
    winner = g.run_game()
    wins[winner.id] += 1

print(f'\nOVERALL WINNER: {"P1" if wins[0] > wins[1] else "P2"} ({wins})')
