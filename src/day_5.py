file = open("../input/day_5.txt").read().strip()


def react_polymer(polymer):
    processed = []
    for c in polymer:
        if processed and c == processed[-1].swapcase():
            processed.pop()
        else:
            processed.append(c)

    return len(processed)


print(react_polymer(file))


def shorten_polymer(polymer):
    units = set([c.lower() for c in polymer])  # set of letters (may not be entire alphabet)

    best = None
    for unit in units:
        candidate = polymer.replace(unit, '').replace(unit.upper(), '')
        length = react_polymer(candidate)
        if best is None or length < best:
            best = length

    return best


print(shorten_polymer(file))
