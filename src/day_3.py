import re
from collections import defaultdict
from itertools import product


# part 1
def overlapping_area(filename):
    file = open(filename, "r")

    # regex from https://old.reddit.com/r/adventofcode/comments/a2lesz/2018_day_3_solutions/eazev7m/
    # much better than the messy string manipulations done before, and does not precompute everything
    claims = map(lambda s: map(int, re.findall(r'-?\d+', s)), file)

    claim_occupancy = dict()
    for claim_id, dist_left, dist_top, width, height in claims:
        for x, y in product(range(dist_left, dist_left + width), range(dist_top, dist_top + height)):
            if (x, y) in claim_occupancy:
                claim_occupancy[(x, y)] = 1
            else:
                claim_occupancy[(x, y)] = 0

    overlaps = sum(claim_occupancy.values())

    return overlaps


# part 2
def non_overlapping_claim(filename):
    file = open(filename, "r")
    claims = map(lambda s: map(int, re.findall(r'-?\d+', s)), file)

    claim_occupancy = defaultdict(set)
    valid_claims = set()
    for claim_id, dist_left, dist_top, width, height in claims:
        valid_claims.add(claim_id)
        for x, y in product(range(dist_left, dist_left + width), range(dist_top, dist_top + height)):
            claim_occupancy[(x, y)].add(claim_id)

    for xy, claims in claim_occupancy.items():
        if len(claims) > 1:
            valid_claims -= claims

    return list(valid_claims)[0]


print(overlapping_area("../input/day_3.txt"))
print(non_overlapping_claim("../input/day_3.txt"))
