from collections import deque

cups = deque(map(int, '156794823'))

for _ in range(100):
    cups.rotate(-1)
    removed = [cups.popleft(), cups.popleft(), cups.popleft()]
    cups.rotate()
    if cups[0]-1 in cups:
        target = cups[0]-1
    else:
        av_cups = [cup for cup in sorted(cups) if cup < cups[0]]
        if cups[0]-1 < min(cups):
            target = max(cups)
        else:
            target = max(av_cups)
    for cup in removed[::-1]: cups.insert(cups.index(target)+1, cup)
    cups.rotate(-1)

while cups[0] != 1: cups.rotate()
cups.popleft()

print('Part 1:', ''.join(map(str, cups)))