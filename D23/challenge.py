class Cup:
    def __init__(self, id):
        self.id = id
        self.next = None

    def get_next(self, n):
        curr = self
        for _ in range(n): curr = curr.next
        return curr

    def __repr__(self):
        return f'Cup{self.id}'


def shuffle_cups(cups, times):
    cups_set = set(cups)
    cups_map = {}
    cups_len = len(cups)
    for i in range(cups_len-1, -1, -1):
        cups_map[cups[i]] = Cup(cups[i])
        cups_map[cups[i]].next = cups_map[cups[i+1]] if i+1 != cups_len else None
    cups_map[cups[-1]].next = cups_map[cups[0]]
    current_cup = cups_map[cups[0]]
    for _ in range(times):
        removed = [
            current_cup.get_next(1),
            current_cup.get_next(2),
            current_cup.get_next(3)
        ]
        removed_id = set([cup.id for cup in removed])
        current_cup.next = current_cup.get_next(4)
        target = current_cup.id-1
        while 1:
            if target in (cups_set - removed_id) or target == 0: break
            target -= 1
        if target not in cups_map:
            target = max(cups_set - removed_id)
        removed[-1].next = cups_map[target].next
        cups_map[target].next = removed[0]
        current_cup = current_cup.next
    return cups_map


cups = [int(cup) for cup in '156794823']
cups_map = shuffle_cups(cups, 100)
print('Part 1:', ''.join(map(str, [cups_map[1].get_next(i+1).id for i in range(len(cups)-1)])))

cups = [int(cup) for cup in '156794823'] + [cup for cup in range(10, 1000001)]
cups_map = shuffle_cups(cups, 10000000)
print('Part 2:', cups_map[1].next.id * cups_map[1].next.next.id)