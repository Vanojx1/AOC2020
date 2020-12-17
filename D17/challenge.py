from functools import reduce
from itertools import product

with open('input') as f:
    chal_input = [l.rstrip() for l in f.readlines()]


class Point:

    def __init__(self, *coords):
        self.dim = len(coords)
        self.coords = coords

    def get_around(self):
        zero = (0,) * self.dim
        return set([self+o for o in product([-1, 0, 1], repeat=self.dim) if o != zero])

    def alive_around(self, current_alive):
        return self.get_around() & current_alive

    def death_around(self, current_alive):
        return self.get_around() - current_alive

    def __hash__(self):
        return hash(self.coords)

    def __eq__(self, p):
        return self.coords == (p if type(p) == tuple else p.coords)

    def __add__(self, p):
        return Point(*map(sum, zip(self.coords, p if type(p) == tuple else p.coords)))

    def __repr__(self):
        return 'P(' + ', '.join(map(str, self.coords)) + ')'


alive_cubes_3d = {Point(x, y, 1) for y, row in enumerate(chal_input) for x, char in enumerate(row) if char == '#'}
alive_cubes_4d = {Point(x, y, 1, 1) for y, row in enumerate(chal_input) for x, char in enumerate(row) if char == '#'}

for _ in range(6):
    alive_cubes_3d = set([cube for cube in alive_cubes_3d if len(cube.alive_around(alive_cubes_3d)) in [2, 3]] + \
                         [cube for cube in reduce(lambda c, n: c|n.death_around(alive_cubes_3d), alive_cubes_3d, set([])) if len(cube.alive_around(alive_cubes_3d)) == 3])
    
    alive_cubes_4d = set([cube for cube in alive_cubes_4d if len(cube.alive_around(alive_cubes_4d)) in [2, 3]] + \
                         [cube for cube in reduce(lambda c, n: c|n.death_around(alive_cubes_4d), alive_cubes_4d, set([])) if len(cube.alive_around(alive_cubes_4d)) == 3])


print('Part 1', len(alive_cubes_3d))
print('Part 2', len(alive_cubes_4d))