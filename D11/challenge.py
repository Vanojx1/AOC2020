with open('input') as f:
    chal_input = [l.rstrip() for l in f.readlines()]

seats = {complex(x, y): s for y, row in enumerate(chal_input) for x, s in enumerate(row)}

def get_occupied(curr_seats):
    def get_around(p): return set(p+o for o in [-1j, 1-1j, 1, 1+1j, 1j, -1+1j, -1, -1-1j] if p+o in curr_seats)
    def get_occupied_around(p): return len([s for s in get_around(p) if curr_seats[s] == '#'])
    def compute_seat(p, s):
        if s == '.': return s
        elif s == 'L': return '#' if get_occupied_around(p) == 0 else 'L'
        return 'L' if get_occupied_around(p) >= 4 else '#'
    old_seats = curr_seats.copy()
    while True:
        curr_seats = {k: compute_seat(k, v) for k, v in curr_seats.items()}
        if curr_seats == old_seats: break
        old_seats = curr_seats.copy()
    return len([s for s in curr_seats.values() if s == '#'])


def get_occupied_v2(curr_seats):
    def get_around(p):
        for o in [-1j, 1-1j, 1, 1+1j, 1j, -1+1j, -1, -1-1j]:
            curr = p+o
            while curr in seats:
                if curr_seats[curr] != '.':
                    yield curr
                    break
                curr += o
    def get_occupied_around(p): return len([s for s in get_around(p) if curr_seats[s] == '#'])
    def compute_seat(p, s):
        if s == '.': return s
        elif s == 'L': return '#' if get_occupied_around(p) == 0 else 'L'
        return 'L' if get_occupied_around(p) >= 5 else '#'
    old_seats = curr_seats.copy()
    while True:
        curr_seats = {k: compute_seat(k, v) for k, v in curr_seats.items()}
        if curr_seats == old_seats: break
        old_seats = curr_seats.copy()
    return len([s for s in curr_seats.values() if s == '#'])


print('Part 1:', get_occupied(seats.copy()))
print('Part 2:', get_occupied_v2(seats.copy()))
