import re

with open('input') as f:
    chal_input = f.read()

fields, my_ticket, tickets = chal_input.split('\n\n')

fields = re.findall(r'([a-z ]+): (\d+)-(\d+) or (\d+)-(\d+)', fields)
num_fields = len(fields)

franges = []
ranges = []
for i, (f, a, b, c, d) in enumerate(fields):
    franges += [(i, f, int(a), int(b)), (i, f, int(c), int(d))]
    ranges += [(int(a), int(b)), (int(c), int(d))]
ranges.sort(key=lambda x: x[0])

my_ticket = re.match(r'your ticket:\n((?:\d+,?)*)', my_ticket).group(1)

tickets = re.findall(r'[0-9,]+', tickets)

mixed_ranges = []
range_part = None
while ranges:
    a, b = ranges.pop(0)
    if len(mixed_ranges) == 0 or range_part is None:
        mixed_ranges.append([a])
        range_part = b
    elif a > range_part:
        mixed_ranges[-1].append(range_part)
        mixed_ranges.append([a])
        range_part = b
    else:
        mixed_ranges[-1].append(b)
        range_part = None
    if len(ranges) == 0 and range_part is not None:
        mixed_ranges[-1].append(range_part)

errors = []
valids = []
for parts in map(lambda x: tuple(map(int, x.split(','))), tickets):
    for part in parts:
        if any(a <= part <= b for a, b in mixed_ranges): continue
        errors.append(part)
    if all(any(a <= part <= b for a, b in mixed_ranges) for part in parts): valids.append(parts)

print('Part 1:', sum(errors))

tickets_fields_map = {i: set(range(len(fields))) for i in range(len(valids[0]))}

for valid in valids:
    for i, v in enumerate(valid):
        tickets_fields_map[i] -= set([i for i, f, a, b in franges if a <= v <= b]) ^ set([i for i, f, a, b in franges if  (v < a or v > b)])

while any(len(v) > 1 for v in tickets_fields_map.values()):
    for k, v in tickets_fields_map.items():
        if len(v) == 1:
            for k1, v1 in tickets_fields_map.items():
                if k != k1:
                    tickets_fields_map[k1] -= v

my_ticket_map = {}
for i, v in enumerate(map(int, my_ticket.split(','))):
    my_ticket_map[fields[list(tickets_fields_map[i])[0]][0]] = v

result = 1
for k, v in my_ticket_map.items():
    if 'departure' in k: result *= v

print('Part 2:', result)