
from common import Input, transpose
import re

def is_triangle(sides):
    "Do these side lengths form a valid triangle?"
    x, y, z = sorted(sides)
    return z < x + y

def parse_ints(text): 
    "All the integers anywhere in text."
    return [int(x) for x in re.findall(r'\d+', text)]

triangles = [parse_ints(line) for line in Input(3)]


def invert(triangles):
    "Take each 3 lines and transpose them."
    for i in range(0, len(triangles), 3):
        yield from transpose(triangles[i:i+3])

# print(transpose([1,2,3]))

# print(triangles)

# print('---------------------------------------')

# for item in invert(triangles):
#     print(item)
# print(invert(triangles))