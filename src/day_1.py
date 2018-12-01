from itertools import cycle


# part 1
def find_frequency(filename):
    file = open(filename, "r")
    contents = file.read().strip().splitlines()
    # sum of all numbers in file
    frequency = sum(int(line) for line in contents)

    return frequency


print(find_frequency("../input/day_1.txt"))


# part 2
def find_repeated_frequency(filename):
    frequency = 0
    frequencies = {frequency}

    file = open(filename, "r")
    contents = file.read().strip().splitlines()
    for line in cycle(contents):
        frequency += int(line)

        # repeat until the updated frequency matches a previous value
        if frequency in frequencies:
            return frequency
        else:
            frequencies.add(frequency)


print(find_repeated_frequency("../input/day_1.txt"))
