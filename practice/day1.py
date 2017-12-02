from common import Input

import re

Point = complex 
N, S, E, W = 1j, -1j, 1, -1 # Unit vectors for headings

def distance(point): 
    "City block distance between point and the origin."
    return abs(point.real) + abs(point.imag)

def how_far(moves):
    "After following moves, how far away from the origin do we end up?"
    loc, heading = 0, N # Begin at origin, heading North
    for (turn, dist) in parse(moves):
        heading *= turn
        loc += heading * dist
    return distance(loc)

def parse(text):
    "Return a list of (turn, distance) pairs from text of form 'R2, L42, ...'"
    turns = dict(L=N, R=S)
    return [(turns[RL], int(d))
           for (RL, d) in re.findall(r'(R|L)(\d+)', text)]

assert distance(Point(3, 4)) == 7 # City block distance; Euclidean distance would be 5
assert parse('R2, L42') == [(S, 2), (N, 42)]
assert how_far("R2, L3") == 5
assert how_far("R2, R2, R2") == 2
assert how_far("R5, L5, R5, R3") == 12

how_far(Input(1).read())