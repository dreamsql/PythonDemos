import re

from itertools import product, chain, permutations
from collections import defaultdict
from functools import lru_cache as cache
from math import factorial
# from common import cat

def ok(record: str) -> bool:
    return not re.search(r'LLL|A.*A', record)


def test_ok():
    
    assert ok('LAPLLP')
    assert not ok('LAPLLL')
    assert not ok('LAPLLA')
    assert ok('APLLPLLP')
    assert not ok('APLLPLLL')
    assert not ok('APLLPLLA')
    return 'pass'

def total_ok_slow(N:int) -> int:
    return quantity(all_strings('LAP', N), ok)

def all_strings(alphabet, N):
    return map(cat, product(alphabet,repeat=N))

def quantity(iterable, pred = bool) -> int:
    return sum(map(pred, iterable))

cat = ''.join

{N: total_ok_slow(N) for N in range(11)}

def next_summary(prev_summary: dict) -> dict:

    summary = defaultdict(int)
    for (A, L), c in prev_summary.items():
        if A < 1 : summary[A+1, 0] += c
        if L < 2 : summary[A, L + 1] += c
        summary[A, 0] += c
    return summary


def total_ok(N) -> int:
    summary = {(0, 0): 1}
    for _ in range(N):
        summary = next_summary(summary)
    return sum(summary.values())


def summary_for(N):
    return {(0,0): 1} if N == 0 else next_summary(summary_for(N -1))


print(' N    ok  summary(N)')
print('----------------------')
for N in range(11):
    assert total_ok(N) == total_ok_slow(N)
    print('{:2}  {:4}  {}'.format(N, total_ok(N), dict(summary_for(N))))