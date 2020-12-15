from collections import defaultdict, deque

chal_input = [int(n) for n in '0,6,1,7,2,19,20'.split(',')]


class Memory:
    def __init__(self, chal_input):
        self.memo = defaultdict(lambda: deque(maxlen=2))
        self.turn = 1
        self.last = None

        for n in chal_input: self.push(n)

    def last_is_first(self):
        return len(self.memo[self.last]) == 1

    def last_turn_diff(self):
        return self.memo[self.last][-1] - self.memo[self.last][-2]

    def push(self, n):
        self.memo[n].append(self.turn)
        self.turn += 1
        self.last = n

    def run_until(self, turn):
        while self.turn <= turn:
            if self.last_is_first(): self.push(0)
            else: self.push(self.last_turn_diff())
        return self.last

    def __repr__(self):
        return str(self.memo)


print('Part 1:', Memory(chal_input).run_until(2020))
print('Part 2:', Memory(chal_input).run_until(30000000))