with open('input') as f:
    chal_input = [l.rstrip() for l in f.readlines()]
    ts, busses = chal_input

ts = int(ts)
busses = {int(b): offset for offset, b in enumerate(busses.split(",")) if b != 'x'}

for bus in busses.keys():
    print(bus, round(ts/bus) * bus - ts)

idlist = [id for id in busses]
step = idlist[0]
start = 0
for id in idlist[1:]:
    delta = busses[id]
    for i in range(start, step*id, step):
        if not (i+delta)%id:
            step = step*id
            start = i

print(start)
