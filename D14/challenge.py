import re
from itertools import product

with open('input') as f:
    chal_input = [l.rstrip() for l in f.readlines()]

memory = {}
for row in chal_input:
    if 'mask' in row:
        current_mask = re.match(r'mask = ([01X]+)', row).group(1)
        stripped_mask = re.sub(r'^(X+)', '', current_mask)
        m1 = int(re.sub(r'X', '1', stripped_mask), 2)
        m2 = int(re.sub(r'X', '0', stripped_mask), 2)
    else:
        address, value = map(int, re.match(r'mem\[(\d+)\] = (\d+)', row).groups())
        memory[address] = value & m1 | m2

print('Part 1:', sum(memory.values()))

memory = {}
for row in chal_input:
    if 'mask' in row:
        current_mask = re.match(r'mask = ([01X]+)', row).group(1)
        current_mask = re.sub(r'^(0+)', '', current_mask)
    else:
        address, value = map(int, re.match(r'mem\[(\d+)\] = (\d+)', row).groups())
        bin_address = bin(address)[2:].zfill(len(current_mask))
        mask = current_mask.zfill(len(bin_address))
        xindices = [i for i, x in enumerate(mask) if x == "X"]
        for comb in product([0, 1], repeat=mask.count('X')):
            curr_mask_map = dict(zip(xindices, comb))
            k = [curr_mask_map[i] if i in curr_mask_map else (int(bin_address[i]) | int(mask[i])) for i in range(len(mask))]
            memory[int(''.join(map(str, k)), 2)] = value

print('Part 2:', sum(memory.values()))
