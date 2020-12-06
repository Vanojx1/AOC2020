from functools import reduce

with open('input') as f:
    chal_input = [l.rstrip() for l in f.readlines()]

maxx = len(chal_input[0])
maxy = len(chal_input)

forest = {(x, y): char for y, row in enumerate(chal_input) for x, char in enumerate(row)}
trees = 0

slope_map = [
    {'o': 1+1j, 'p': 0, 't': 0},
    {'o': 3+1j, 'p': 0, 't': 0},
    {'o': 5+1j, 'p': 0, 't': 0},
    {'o': 7+1j, 'p': 0, 't': 0},
    {'o': 1+2j, 'p': 0, 't': 0}
]

for y in range(maxy):
    for slope in slope_map:
        p = (slope['p'].real % maxx, slope['p'].imag)
        if p in forest and forest[p] == '#': slope['t'] += 1
        slope['p'] += slope['o']

print('Part 1:', slope_map[1]['t'])
print('Part 2:', reduce(lambda c, n: c*n['t'], slope_map, 1))