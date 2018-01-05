from collections import deque, Counter

from itertools import product, combinations

import random


Coins = ''.join

Belief = frozenset

all_coins = Belief(map(Coins, product('HT', repeat=4)))


print(all_coins)