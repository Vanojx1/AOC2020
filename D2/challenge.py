import re
from collections import Counter

with open('input') as f:
    chal_input = [l.rstrip() for l in f.readlines()]

def get_valid_p1():
    for row in chal_input:
        vmin, vmax, char, passw = re.match(r'(\d+)-(\d+) (\w): (\w+)', row).groups()
        count = Counter(passw)
        if char not in count: continue
        if int(vmin) <= count[char] <= int(vmax): yield passw

def get_valid_p2():
    for row in chal_input:
        p1, p2, char, passw = re.match(r'(\d+)-(\d+) (\w): (\w+)', row).groups()
        p1 = int(p1)-1
        p2 = int(p2)-1
        c1 = passw[p1] if p1 < len(passw) else None
        c2 = passw[p2] if p2 < len(passw) else None
        if (c1 == char or c2 == char) and c1 != c2: yield passw

print('Part 1:', len(list(get_valid_p1())))
print('Part 2:', len(list(get_valid_p2())))