import re
from operator import add, mul

with open('input') as f:
    chal_input = [l.rstrip() for l in f.readlines()]

op_map = {'+': add, '*': mul}


def a_op_b(m):
    a, op, b = m.groups()
    return str(op_map[op](int(a), int(b)))


def resolve_add_mul(expr):
    while 1:
        expr, c = re.subn(r'(\d+) (\+) (\d+)', a_op_b, expr, count=1)
        if c == 0: break
    while 1:
        expr, c = re.subn(r'(\d+) (\*) (\d+)', a_op_b, expr, count=1)
        if c == 0: break
    return expr


def resolve_left_right(expr):
    while 1:
        expr, c = re.subn(r'(\d+) ([+*]) (\d+)', a_op_b, expr, count=1)
        if c == 0: break
    return expr


def resolve_brackets(expr, resolver):
    while 1:
        expr, c = re.subn(r'\(([^()]+)\)', lambda m: resolver(m.group(1)), expr, count=1)
        if c == 0: break
    return int(resolver(expr))


print('Part 1', sum(map(lambda expr: resolve_brackets(expr, resolve_left_right), chal_input)))
print('Part 2', sum(map(lambda expr: resolve_brackets(expr, resolve_add_mul), chal_input)))
