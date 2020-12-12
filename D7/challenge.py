import re
from functools import reduce

with open('input') as f:
    chal_input = [l.rstrip() for l in f.readlines()]

bag_dictionary = {}
for row in chal_input:
    bag, str_content = re.match(r'([a-z ]*?) bags contain ([a-z0-9 ,]+)', row).groups()
    bag_dictionary[bag] = [re.match(r'(\d+) ([a-z ]+?) bags?', bag).groups() for bag in str_content.split(', ') if bag != 'no other bags']

def open_bags(q, bag):
    # print(q, bag)
    inside = bag_dictionary[bag]
    return reduce(lambda c, n: [*c, n[1], *open_bags(*n)], inside, [])

def count_bags(q, bag):
    inside = bag_dictionary[bag]
    return int(q) * sum(int(b[0]) + count_bags(*b) for b in inside)

shiny_gold = 0
for bag in bag_dictionary.keys():
    if 'shiny gold' in open_bags(0, bag):
        shiny_gold += 1

print('Part 1:', shiny_gold)
print('Part 2:', count_bags(1, 'shiny gold'))