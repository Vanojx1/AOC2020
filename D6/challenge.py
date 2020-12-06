from functools import reduce

with open('input') as f:
    chal_input = [group.split("\n") for group in f.read().split("\n\n")]

total_yes = 0
everyone_yes = 0
for g in chal_input:
    total_yes += len(set.union(*map(set, g)))
    everyone_yes += len(set.intersection(*map(set, g)))

print('Part 1:', total_yes)
print('Part 2:', everyone_yes)
