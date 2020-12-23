import re

with open('input') as f:
    p1_cards, p2_cards = re.findall(r'Player [12]:\n((?:\d+\n?)+)', f.read())
    p1_cards = [int(c) for c in p1_cards[:-1].split('\n')]
    p2_cards = [int(c) for c in p2_cards.split('\n')]


def combat(p1_cards, p2_cards):
    while 1:
        if len(p1_cards) == 0:
            return sum((i+1)*c for i, c in enumerate(p2_cards[::-1]))
        elif len(p2_cards) == 0:
            return sum((i+1)*c for i, c in enumerate(p1_cards[::-1]))
        c1 = p1_cards.pop(0)
        c2 = p2_cards.pop(0)
        if c1 > c2:
            p1_cards += [c1, c2]
        else:
            p2_cards += [c2, c1]


def recursive_combat(p1_cards, p2_cards, game_id=1):
    game_history = set([])
    while 1:
        str_turn = f'{p1_cards}-{p2_cards}'
        if len(p1_cards) == 0:
            if game_id == 1: return sum((i+1)*c for i, c in enumerate(p2_cards[::-1]))
            return 0
        elif len(p2_cards) == 0 or str_turn in game_history:
            if game_id == 1: return sum((i+1)*c for i, c in enumerate(p1_cards[::-1]))
            return 1
        game_history.add(str_turn)
        c1 = p1_cards.pop(0)
        c2 = p2_cards.pop(0)
        if c1 <= len(p1_cards) and c2 <= len(p2_cards):
            winner = recursive_combat(p1_cards[:c1].copy(), p2_cards[:c2].copy(), game_id+1)
        else:
            winner = c1 > c2
        if winner:
            p1_cards += [c1, c2]
        else:
            p2_cards += [c2, c1]


print('Part 1:', combat(p1_cards.copy(), p2_cards.copy()))
print('Part 2:', recursive_combat(p1_cards.copy(), p2_cards.copy()))
