

def pairs(collection):
    return [(A,B) for A in collection for B in collection if A <= B]


def sums(pair):
    (A, B) = pair
    return Bag(a + b for a in A for b in B)

Bag = sorted


def ints(start, end):
    return tuple(range(start, end + 1))

regular_die = ints(1, 6)
regular_pair = (regular_die, regular_die)
regular_sums = sums(regular_pair)
