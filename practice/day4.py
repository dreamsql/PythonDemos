import re
from common import cat

from collections import Counter


def parse(line): 
    "Return (name, sector, checksum)."
    return re.match(r"(.+)-(\d+)\[([a-z]+)\]", line).groups()

def sector(line):
    "Return the sector number if valid, or 0 if not."
    name, sector, checksum = parse(line)
    return int(sector) if valid(name, checksum) else 0

def valid(name, checksum):
    "Determine if name is valid according to checksum."
    counts = Counter(name.replace('-', '')) 
    print(counts)
    # Note: counts.most_common(5) doesn't work because it breaks ties arbitrarily.
    letters = sorted(counts, key=lambda L: (-counts[L], L))
    print(letters)
    return checksum == cat(letters[:5])

# assert  parse('aaaaa-bbb-z-y-x-123[abxyz]') == ('aaaaa-bbb-z-y-x', '123', 'abxyz')
# assert sector('aaaaa-bbb-z-y-x-123[abxyz]') == 123
assert  valid('aaaaa-bbb-z-y-x', 'abxyz')