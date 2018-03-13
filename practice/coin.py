from collections import deque, Counter

from itertools import product, combinations

import random


Coins = ''.join

Belief = frozenset

all_coins = Belief(map(Coins, product('HT', repeat=4)))


def rotations(coins)  -> [Coins]:
    return [coins[r:] + coins[:r] for r in range(4)]