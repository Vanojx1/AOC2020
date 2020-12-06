with open('input') as f:
    chal_input = [int(l.rstrip()) for l in f.readlines()]

min_val = min(chal_input)

def get_2020_by2():
	for n1 in chal_input:
		if n1+min_val > 2020: continue
		for n2 in chal_input:
			if n1+n2 == 2020: return n1*n2

def get_2020_by3():
	for n1 in chal_input:
		if n1+min_val > 2020: continue
		for n2 in chal_input:
			if n1+n2 > 2020: continue
			for n3 in chal_input:
				if n1+n2+n3 == 2020: return n1*n2*n3
		

print('Part 1:', get_2020_by2())
print('Part 2:', get_2020_by3())