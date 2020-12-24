import re
from functools import reduce

with open('input') as f:
    chal_input = [re.findall(r'e|w|se|ne|sw|nw', l.rstrip()) for l in f.readlines()]


move_mapping = {
    'e': 2,
    'sw': -1+1j,
    'se': 1+1j,
    'w': -2,
    'nw': -1-1j,
    'ne': 1-1j,
}

black_tiles = set([])
for row in chal_input:
    position = 0j
    for move in row:
        position += move_mapping[move]
    if position in black_tiles: black_tiles.remove(position)
    else: black_tiles.add(position)


def get_around(tile):
    return set([tile+offset for offset in move_mapping.values()])


def n_black_around(tile, bt):
    return len([a for a in get_around(tile) if a in bt])


def white_around(tile, bt):
    return set([a for a in get_around(tile) if a not in bt])


print('Part 1:', len(black_tiles))

for _ in range(100):
    relevant_white_tiles = reduce(lambda c, n: c | white_around(n, black_tiles), black_tiles, set([]))
    black_tiles = {tile for tile in black_tiles if n_black_around(tile, black_tiles) in [1, 2]} | \
                  {tile for tile in relevant_white_tiles if n_black_around(tile, black_tiles) == 2}

print('Part 2:', len(black_tiles))