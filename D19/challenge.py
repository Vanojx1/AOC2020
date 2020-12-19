import re

with open('input') as f:
    chal_input = [l.rstrip() for l in f.readlines()]
	
rules = {}
messages = []
for row in chal_input:
	m = re.match(r'^(\d+): "?([0-9 |a-z]+)"?$', row)
	if m: rules[m.group(1)] = m.group(2)
	
	m = re.match(r'^(\w+)$', row)
	if m: messages.append(m.group(1))

def resolve(m):
	if rules[m.group(1)] in ['a', 'b']: return rules[m.group(1)]
	return '(?:' + re.sub(r'(\d+)', resolve, rules[m.group(1)]) + ')'

resolved_resules = {}
for k, rule in rules.items():
	if rule in ["a", "b"]: continue
	resolved_resules[k] = re.sub(r'(\d+)', resolve, rule).replace(' ', '')

matching_messages = 0
for message in messages:
	if re.match(re.compile('^' + resolved_resules['0'] + '$'), message): matching_messages += 1

print('Part 1:', matching_messages)

rules['8'] = "42 | 42 [ab]"
rules['11'] = "42 31 | 42 [ab] 31"

resolved_resules = {}
for k, rule in rules.items():
	if rule in ["a", "b"]: continue
	resolved_resules[k] = re.sub(r'(\d+)', resolve, rule).replace(' ', '')
	print(k, resolved_resules[k])

matching_messages = 0
for message in messages:
	if re.match(re.compile('^' + resolved_resules['0'] + '$'), message): matching_messages += 1

print('Part 2:', matching_messages)