from collections import Counter

# part 1
from itertools import combinations


def checksum(filename):
    file = open(filename, "r")
    contents = file.read().strip().splitlines()
    boxes_with_double = 0  # times that a code has 2 repeated letters
    boxes_with_triple = 0  # times that a code has 3 repeated letters
    for line in contents:
        letter_count = [j for i, j in Counter(line).most_common()]  # count number of times letters are repeated
        # update counts as necessary
        if 2 in letter_count:
            boxes_with_double += 1
        if 3 in letter_count:
            boxes_with_triple += 1

    return boxes_with_double * boxes_with_triple  # checksum is result of multiplying both counts


print(checksum("../input/day_2.txt"))


# part 2
def correct_boxes(filename):
    file = open(filename, "r")
    contents = file.read().strip().splitlines()
    for code_1, code_2 in combinations(contents, 2):  # iterate over all combinations of codes
        differences = 0  # number of letters that are different in a pairwise iteration over both codes
        for i, j in zip(code_1, code_2):
            if i != j:
                differences += 1

        if differences == 1:  # correct codes are off by 1
            common_letters = ""
            for i, j in zip(code_1, code_2):  # find letters which are in common
                if i == j:
                    common_letters += i

            return common_letters


print(correct_boxes("../input/day_2.txt"))
