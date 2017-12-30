import re 
import unittest

program = '''
10 REM POWER TABLE
11 DATA 8,  4
15 READ N0, P0
20 PRINT "N",
25 FOR P = 2 to P0
30   PRINT "N ^" P,
35 NEXT P
40 PRINT "SUM"
45 LET S = 0
50 FOR N = 2 TO N0
55   PRINT N,
60   FOR P = 2 TO P0
65     LET S = S + N ^ P
70     PRINT N ^ P,
75   NEXT P
80   PRINT S
85 NEXT N
99 END
'''


tokenize = re.compile(
    r'''\d* \.? \d+ (?: E -? \d+)?                 | # number 
    SIN|COS|TAN|ATN|EXP|ABS|LOG|SQR|RND|INT|FN[A-Z]| # functions (including user-defined FNA-FNZ)
    LET|READ|DATA|PRINT|GOTO|IF|FOR|NEXT|END|STOP  | # keywords
    DEF|GOSUB|RETURN|DIM|REM|TO|THEN|STEP          | # more keywords
    [A-Z]\d? | # variable names (letter optionally followed by a digit)
    " .*? "  | # labels (strings in double quotes)
    <>|>=|<= | # multi-character relational operators
    \S       ''' , # any non-space single character , 
    re.VERBOSE).findall


tokens = []


def peek():
    return tokens[0] if tokens else None

def tokennizer(line):
    return tokenize(remove_spaces(line).upper())

def pop(constraint=None):
    if constraint is None or (peek() == constraint) or (callable(constraint) and constraint(peek())):
        return tokens.pop(0)


def  remove_spaces(line):
    return ''.join(tokenize(line))

def lines(text):
    return [line for line in text.splitlines() if line]




class TestTokenizer(unittest.TestCase):
    def test(self):
        self.assertEqual( tokennizer('X-1'),['X', '-', '1'] )
        self.assertEqual(tokennizer('PRINT "HELLO WORLD"'), ['PRINT', '"HELLO WORLD"'])
        self.assertEqual(tokennizer('10 GOTO 99'), ['10', 'GOTO', '99'])
        self.assertEqual(tokennizer('10GOTO99'), ['10', 'GOTO', '99'])
        self.assertEqual(tokennizer('10 GO TO 99'), ['10', 'GOTO', '99'])
        self.assertEqual(tokennizer('100 PRINT "HELLO WORLD", SIN(X) ^ 2'), ['100', 'PRINT', '"HELLO WORLD"', ',', 'SIN', '(', 'X', ')', '^', '2'])
        self..assertEqual(tokennizer('100IFX1+123.4+E1-12.3E4 <> 1.2E-34*-12E34+1+"HI" THEN99'),['100', 'IF', 'X1', '+', '123.4', '+', 'E1', '-', '12.3E4', '<>', '1.2E-34', '*', '-', '12E34', '+', '1', '+', '"HI"', 'THEN', '99'])
        self.assertEqual(remove_spaces('10 GO TO 99'), '10GOTO99')
        self.assertEqual(remove_spaces('100 PRINT "HELLO WORLD", SIN(X) ^ 2'), '100PRINT"HELLO WORLD",SIN(X)^2')
        self.assertEqual(lines('one line'), ['one line'])



if __name__ == '__main__':
    unittest.main()

# def test_tokenizer():
#     global tokens

#     assert tokennizer('X-1') == ['X', '-', '1']

# if __name__ == "__main__":
#     test_tokenizer()




    


    