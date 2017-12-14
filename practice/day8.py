import numpy as np
import re
from common import Input,cat

def interpret(cmd, screen):
    A, B = map(int, re.findall(r'(\d+)', cmd))
    if cmd.startswith('rect'):
        screen[:B, :A] = 1
    elif cmd.startswith('rotate row'):
        screen[A, :] = rotate(screen[A,:], B)
    elif cmd.startswith('rotate col'):
        screen[:,A] = rotate(screen[:, A], B)
        

def rotate(items, n): return np.append(items[-n:], items[:-n])

def Screen(): return np.zeros((6, 50), dtype = np.int)

def run(commands, screen):
    for cmd in commands:
        interpret(cmd,screen)
    return screen


screen = run(Input(8), Screen())
print(np.sum(screen))
for row in screen:
    # print(cat(' @'[pixel] for pixel in row))
    #  print([' @'[pixel] for pixel in row])
    # print([[pixel] for pixel in row])
    print(cat( ' @' if pixel == 1 else '  ' for pixel in row))


# a = np.zeros((6,6), dtype=int)

# b = [1,2, 3]

# c = [' @'[m] for m in b]
# print(c)