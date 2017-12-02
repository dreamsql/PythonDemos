import re
import unittest

def abba(text):
    return any(a == d != b == c for (a, b, c, d) in subsequences(text, 4))

def subsequences(seq, n):
    # print(seq)
    return [seq[i: i + n] for i in range(len(seq) + 1 - n)]

def segement(line):
    return re.split(r'\[|\]',line)

def outsides(segments):
    return ', '.join(segments[0::2])

def insides(segements): return ', '.join(segements[1::2])

def tls(segements):
    return abba(outsides(segements)) and not abba(insides(segements))

alphabet = 'abcdefghijklmnopqrstuvwxyz'
def ssl(segements):
    outs, ins = outsides(segements), insides(segements)
    return any(a + b + a in outs and b + a + b in ins
               for a in alphabet for b in alphabet if a != b)
    

# print(subsequences('abbe', 4))
class Test(unittest.TestCase):
    def test(self):
        #  abba('abba') and not abba('aaaa')
        # assert subsequences('abcde', 4) == ['abcd', 'bcde']
        # assert outsides(['1111', '2222', '3333', '4444']) == '1111, 3333'
        # assert insides(['1111', '2222', '3333', '4444']) == '2222, 4444'
        self.assertEqual(segement('aaaa[bbbb]cddc[1234]zz') ,['aaaa','bbbb','cddc','1234', 'zz'])
        self.assertEqual(tls(segement('aaaa[bbbb]cddc[1234]zz')), True)
        self.assertEqual(tls(segement('aaaa[bbbb]cdcd[1234]zz')), False)
        self.assertEqual(ssl(segement('aaaa[bbbb]aba[1234]zz[bab]')), True)




