import re
from collections import defaultdict, Counter

with open('input') as f:
    chal_input = [l.rstrip() for l in f.readlines()]

ingr_map = defaultdict(int)
detail_ingr_map = defaultdict(int)

count = Counter()
allergens_all = set([])

for row in chal_input:
    ingredients, allergens = re.match(r'((?:\w+ ?)*?) \(contains ((?:\w+(?:, )?)+)+\)', row).groups()
    ingredients = ingredients.split(' ')
    allergens = allergens.split(', ')
    for ingr in ingredients:
        ingr_map[ingr] += len(allergens) / len(ingredients) * 100
    
    for ingr in ingredients:
        for al in allergens:
            detail_ingr_map[(ingr, al)] += len(allergens) / len(ingredients) * 100

    count += Counter(ingredients)
    allergens_all |= set(allergens)

sorted_probs = sorted(ingr_map.items(), key=lambda x: x[1])
q = [k for k, v in sorted_probs[:-len(allergens_all)]]

print('Part 1:', sum([v for k, v in count.items() if k in q]))

allergens_map = {}
while len(allergens_map) != len(allergens_all):
    for al in allergens_all:
        if al in allergens_map.values(): continue
        al_sorted_probs = sorted([(k, v) for k, v in detail_ingr_map.items() if k[1] == al and k[0] not in allergens_map], key=lambda x: -x[1])
        max_prob = max(al_sorted_probs, key=lambda x: x[1])[1]
        ingr_with_max_prob = [(k, v) for k, v in al_sorted_probs if v == max_prob]
        if len(ingr_with_max_prob) == 1:
            allergens_map[ingr_with_max_prob[0][0][0]] = ingr_with_max_prob[0][0][1]
            break

print('Part 2:', ','.join(sorted(allergens_map, key=allergens_map.get)))