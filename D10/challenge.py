from collections import defaultdict
from functools import reduce

with open('input') as f:
    chal_input = [int(l.rstrip()) for l in f.readlines()]

sorted_ad = sorted(chal_input)
max_jolts = max(sorted_ad) + 3


def chain_ad(curr_jolts, jolt_diffs):
    next_ad = min([j for j in sorted_ad if curr_jolts < j <= curr_jolts+3] + [max_jolts])
    jolt_diffs[next_ad - curr_jolts] += 1
    if next_ad == max_jolts: return jolt_diffs
    return chain_ad(next_ad, jolt_diffs)


chain = chain_ad(0, defaultdict(int))


def calc_chains():
    XMAS = [0] + sorted_ad + [max_jolts]
    POW2 = 0
    POW7 = 0
    for i in range(len(XMAS)-1):
        n3 = XMAS[i - 3] if i >= 3 else -9999
        if XMAS[i + 1] - n3 == 4:
            POW7 += 1
            POW2 -= 2
        elif XMAS[i + 1] - XMAS[i - 1] == 2:
            POW2 += 1
    return (2**POW2) * (7**POW7)


print('Part 1:', reduce(lambda c, n: c*n, chain.values(), 1))
print('Part 2:', calc_chains())
