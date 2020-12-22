import re
import math
import numpy as np

with open('input') as f:
    chal_input = f.read().split('\n\n')

TILE_SIZE = 10
TILE_N = int(math.sqrt(len(chal_input)))


class Tile:
    def __init__(self, id, r, matrix):
        self.id = int(id)
        self.r = r
        self.matrix = matrix
        self.tile_map = {complex(x, y): v for y, row in enumerate(self.matrix) for x, v in enumerate(row)}
        self.borders = {
            'U': ''.join([self.tile_map[complex(x, 0)] for x in range(TILE_SIZE)]),
            'R': ''.join([self.tile_map[complex(TILE_SIZE-1, y)] for y in range(TILE_SIZE)]),
            'B': ''.join([self.tile_map[complex(x, TILE_SIZE-1)] for x in range(TILE_SIZE)]),
            'L': ''.join([self.tile_map[complex(0, y)] for y in range(TILE_SIZE)])
        }
        self.matching = {}

    @property
    def index(self):
        return f'{self.id}-{self.r}'

    def calc_matching(self, tiles):
        self.matching = {
            'U': [t for t in tiles if t.id != self.id and t.borders['B'] == self.borders['U']],
            'R': [t for t in tiles if t.id != self.id and t.borders['L'] == self.borders['R']],
            'B': [t for t in tiles if t.id != self.id and t.borders['U'] == self.borders['B']],
            'L': [t for t in tiles if t.id != self.id and t.borders['R'] == self.borders['L']]
        }
    def __repr__(self):
        return f'Tile({self.id}, {self.r})'
    def __lt__(self, o):
        return self.index < o.index
    def __eq__(self, o):
        return self.index == o.index
    def __hash__(self):
        return hash(self.index)


matrixes = [
    ('0',     lambda x: x),
    ('90',    lambda x: np.rot90(x, -1)),
    ('180',   lambda x: np.rot90(x, -2)),
    ('270',   lambda x: np.rot90(x, -3)),
    ('UD',    lambda x: np.flipud(x)),
    ('UD90',  lambda x: np.rot90(np.flipud(x), -1)),
    ('UD180', lambda x: np.rot90(np.flipud(x), -2)),
    ('UD270', lambda x: np.rot90(np.flipud(x), -3)),
    ('LR',    lambda x: np.fliplr(x)),
    ('LR90',  lambda x: np.rot90(np.fliplr(x), -1)),
    ('LR180', lambda x: np.rot90(np.fliplr(x), -2)),
    ('LR270', lambda x: np.rot90(np.fliplr(x), -3)),
]

tiles = []
for tile_str in chal_input:
    id = re.match(r'Tile (\d+):\n', tile_str).group(1)
    raw = re.sub(r'Tile \d+:\n', '', tile_str)
    matrix = np.array([list(row) for row in raw.split('\n')])
    for suffix, matrix_fn in matrixes:
        tiles.append(Tile(id, suffix, matrix_fn(matrix)))

[t.calc_matching(tiles) for t in tiles]

start_tiles = []

for tile in tiles:
    if len(tile.matching['L']) + len(tile.matching['U']) == 0 and len(tile.matching['B']) > 0 and len(tile.matching['R']) > 0:
        start_tiles.append(tile)

tileq = []
for tile in start_tiles:
    tileq.append((1, tile, 0, 0, 1, {(0, 0): tile}))


def assemble_image():
    while tileq:
        placed_n, current, nx, ny, next_dir, placed = tileq.pop()

        if placed_n == len(chal_input):
            return placed

        placed_id = [t.id for t in placed.values()]

        if next_dir == 1 and nx < TILE_N-1:
            next_tiles = [t for t in current.matching['R'] if t.id not in placed_id]
            nx += next_dir
        elif next_dir == 1 and nx == TILE_N-1:
            next_tiles = [t for t in current.matching['B'] if t.id not in placed_id]
            ny += 1
            next_dir = -1
        elif next_dir == -1 and nx > 0:
            next_tiles = [t for t in current.matching['L'] if t.id not in placed_id]
            nx += next_dir
        elif next_dir == -1 and nx == 0:
            next_tiles = [t for t in current.matching['B'] if t.id not in placed_id]
            ny += 1
            next_dir = 1

        for tile in next_tiles:
            tileq.append((placed_n+1, tile, nx, ny, next_dir, {**{(nx, ny): tile}, **placed}))

tile_map = assemble_image()

print('Part 1:', tile_map[(0, 0)].id * tile_map[(TILE_N-1, 0)].id * tile_map[(0, TILE_N-1)].id * tile_map[(TILE_N-1, TILE_N-1)].id)

bitmap = {}
for cy in range(TILE_N):
    for cx in range(TILE_N):
        for y in range(1, TILE_SIZE-1):
            for x in range(1, TILE_SIZE-1):
                xy = (cx*(TILE_SIZE-2)+x-1, cy*(TILE_SIZE-2)+y-1)
                bitmap[complex(*xy)] = tile_map[(cx, cy)].matrix[y][x]

bitmap_arr = []
for y in range((TILE_SIZE-2)*TILE_N):
    bitmap_arr.append([bitmap[complex(x, y)] for x in range((TILE_SIZE-2)*TILE_N)])

raw_monster = [list(row) for row in "                  # \n#    ##    ##    ###\n #  #  #  #  #  #   ".split('\n')]
monster = {complex(x, y) for y, row in enumerate(raw_monster) for x, v in enumerate(row) if v == '#'}

for _, matrix_fn in matrixes:
    curr_matrix = matrix_fn(bitmap_arr)
    current = {complex(x, y) for y, row in enumerate(curr_matrix) for x, v in enumerate(row) if v == '#'}
    matching_monsters = set([])
    for offset in bitmap.keys():
        current_monster = {m+offset for m in monster}
        if len(current_monster - current) == 0:
            matching_monsters |= current_monster
    if matching_monsters:
        for xy in matching_monsters:
            curr_matrix[int(xy.imag)][int(xy.real)] = 'O'
        print('Part 2:', np.count_nonzero(curr_matrix == '#'))
        break
