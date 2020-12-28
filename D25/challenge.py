def transform(subject, loop_size):
    n = 1
    for _ in range(loop_size):
        n *= subject
        n %= 20201227
    return n


def find_loop(subject, key):
    n = 1
    loop_size = 1
    while 1:
        n *= subject
        n %= 20201227
        if n == key: break
        loop_size += 1
    return loop_size


card_key = 15335876 # 5764801
door_key = 15086442 # 17807724

print('Part 1:', transform(card_key, find_loop(7, door_key)))