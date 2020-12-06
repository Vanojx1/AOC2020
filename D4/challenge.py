import re

with open('input') as f:
    chal_input = re.sub(r'\n([^\n])', r' \1', f.read()).split('\n')

fields = [
    ('byr', r'(\d{4})', lambda x: x is not None and 1920 <= int(x.group(1)) <= 2002),
    ('iyr', r'(\d{4})', lambda x: x is not None and 2010 <= int(x.group(1)) <= 2020),
    ('eyr', r'(\d{4})', lambda x: x is not None and 2020 <= int(x.group(1)) <= 2030),
    ('hgt', r'(\d+)(cm|in)', lambda x: x is not None and ((150 <= int(x.group(1)) <= 193) if x.group(2) == 'cm' else (59 <= int(x.group(1)) <= 76))),
    ('hcl', r'#([0-9a-f]{6})', lambda x: x is not None),
    ('ecl', r'(amb|blu|brn|gry|grn|hzl|oth)', lambda x: x is not None),
    ('pid', r'(\d{9})', lambda x: x is not None)
]

def get_valids(strict=False):
    valids = 0
    word_bound = r'\b'
    for passport in chal_input:
        if all(fn(re.search(re.compile(f'{prefix}:{value}{word_bound}'), passport)) if strict else prefix in passport for prefix, value, fn in fields): valids += 1
    return valids


print('Part 1:', get_valids())
print('Part 2:', get_valids(True))
