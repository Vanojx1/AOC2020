with open('input') as f:
    chal_input = [l.rstrip() for l in f.readlines()]

def seat_finder(lpart, upart, parts):
    if len(parts) == 0: return lpart
    if upart - lpart == 1: return lpart * 8 + seat_finder(0, 8, parts)
    part = parts.pop(0)
    half = (upart+lpart)//2
    if part in 'FL':
        return seat_finder(lpart, half, parts)
    elif part in 'BR':
        return seat_finder(half, upart, parts)


seat_ids = [seat_finder(0, 128, list(seat)) for seat in chal_input]
print('Part 1:', max(seat_ids))

for id in range(min(seat_ids), max(seat_ids)+1):
    if id not in seat_ids:
        print('Part 2:', id)
        break