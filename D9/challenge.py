from itertools import combinations

with open('input') as f:
    chal_input = [int(l.rstrip()) for l in f.readlines()]


def get_invalid():
    for i, n in list(enumerate(chal_input))[25:]:
        if n not in [a+b for a, b in combinations(chal_input[i-25:i], 2)]: return n


invalid_number = get_invalid()

print('Part 1:', invalid_number)


def get_weakness():
    nums = len(chal_input)
    for i, n in enumerate(chal_input[:-1]):
        for k in range(i+1, nums):
            if sum(chal_input[i:k]) == invalid_number: return min(chal_input[i:k]) + max(chal_input[i:k])


print('Part 2:', get_weakness())
