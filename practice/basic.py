import re 
import unittest
import math
import operator as op
import random

from collections import namedtuple, defaultdict, deque


Stmt = namedtuple('Stmt', 'num, typ, args')
Subscript = namedtuple('Subscript', 'var, indexes')
Funcall = namedtuple('Funcall', 'f, x')
Opcall = namedtuple('Opcall', 'x, op, y')
ForState = namedtuple('ForState', 'continu, end, step')

variables = {}
functions = {}

class Function(namedtuple('_', 'parm, body')):
    def __call__(self, value):
        variables[self.parm] = value
        return evalu(self.body)



def evalu(exp):
    
    if isinstance(exp, Opcall):
        return functions[exp.op](evalu(exp.x), evalu(exp.y))
    elif isinstance(exp, Funcall):
        return functions[exp.f](evalu(exp.x))
    elif isinstance(exp, Subscript):
        return variables[exp.var, tuple(evalu(x) for x in exp.indexes)]
    elif is_varname(exp):
        return variables[exp]
    else:
        return exp
        
def let(V, value):
    if isinstance(V, Subscript):
        variables[V.var, tuple(evalu(x) for x in V.indexes)] = value
    else:
        variables[V] = value
    

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
    return [line.strip() for line in text.splitlines() if line.strip()]




class TestTokenizer(unittest.TestCase):
    def test(self):
        self.assertEqual( tokennizer('X-1'),['X', '-', '1'] )
        self.assertEqual(tokennizer('PRINT "HELLO WORLD"'), ['PRINT', '"HELLO WORLD"'])
        self.assertEqual(tokennizer('10 GOTO 99'), ['10', 'GOTO', '99'])
        self.assertEqual(tokennizer('10GOTO99'), ['10', 'GOTO', '99'])
        self.assertEqual(tokennizer('10 GO TO 99'), ['10', 'GOTO', '99'])
        self.assertEqual(tokennizer('100 PRINT "HELLO WORLD", SIN(X) ^ 2'), ['100', 'PRINT', '"HELLO WORLD"', ',', 'SIN', '(', 'X', ')', '^', '2'])
      
        self.assertEqual(remove_spaces('10 GO TO 99'), '10GOTO99')
        self.assertEqual(remove_spaces('100 PRINT "HELLO WORLD", SIN(X) ^ 2'), '100PRINT"HELLO WORLD",SIN(X)^2')
        self.assertEqual(lines('one line'), ['one line'])

        self.assertEqual(tokennizer('100IFX1+123.4+E1-12.3E4 <> 1.2E-34*-12E34+1+"HI" THEN99'), ['100', 'IF', 'X1', '+', '123.4', '+', 'E1', '-', '12.3E4', '<>', '1.2E-34', '*', '-', '12E34', '+', '1', '+', '"HI"', 'THEN', '99'])



        self.assertEqual(lines(program), [
        '10 REM POWER TABLE',
        '11 DATA 8,  4',
        '15 READ N0, P0',
        '20 PRINT "N",',
        '25 FOR P = 2 to P0',
        '30   PRINT "N ^" P,',
        '35 NEXT P',
        '40 PRINT "SUM"',
        '45 LET S = 0',
        '50 FOR N = 2 TO N0',
        '55   PRINT N,',
        '60   FOR P = 2 TO P0',
        '65     LET S = S + N ^ P',
        '70     PRINT N ^ P,',
        '75   NEXT P',
        '80   PRINT S',
        '85 NEXT N',
        '99 END'])

        self.assertEqual([tokennizer(line) for line in lines(program)], [
        ['10', 'REM', 'P', 'O', 'W', 'E', 'R', 'T', 'A', 'B', 'L', 'E'],
        ['11', 'DATA', '8', ',', '4'],
        ['15', 'READ', 'N0', ',', 'P0'],
        ['20', 'PRINT', '"N"', ','],
        ['25', 'FOR', 'P', '=', '2', 'TO', 'P0'],
        ['30', 'PRINT', '"N ^"', 'P', ','],
        ['35', 'NEXT', 'P'],
        ['40', 'PRINT', '"SUM"'],
        ['45', 'LET', 'S', '=', '0'],
        ['50', 'FOR', 'N', '=', '2', 'TO', 'N0'],
        ['55', 'PRINT', 'N', ','],
        ['60', 'FOR', 'P', '=', '2', 'TO', 'P0'],
        ['65', 'LET', 'S', '=', 'S', '+', 'N', '^', 'P'],
        ['70', 'PRINT', 'N', '^', 'P', ','],
        ['75', 'NEXT', 'P'],
        ['80', 'PRINT', 'S'],
        ['85', 'NEXT', 'N'],
        ['99', 'END']]) 

        global tokens
        tokens = tokennizer('10 GO TO 99')
        self.assertEqual(peek(),'10')
        self.assertEqual(pop(), '10')
        self.assertEqual(peek(), 'GOTO')
        self.assertEqual(pop(), 'GOTO')
        self.assertEqual(peek(), '99')
        self.assertFalse(pop(str.isalpha))
        self.assertFalse(pop('98.6'))
        self.assertEqual(pop(str.isnumeric), '99')
        self.assertTrue(peek() == None and not tokens)





def linenumber():
    return (int(pop()) if peek().isnumeric() else fail('missing line number {}'.format(peek())))

def number():
    return (-1 if pop('-') else +1)  * float(pop())

def step():
    return (expression() if pop('STEP') else 1)

def relational():
    return pop(is_relational) or fail('expected a relational operator')

def varname():
    return pop(is_varname) or fail('expected a variable name')

def funcname():
    return pop(is_funcname) or fail('expected a function name')

def anycharacters():
    tokens.clear()

def is_stmt_type(x):
    return isinstance(x, str) and x in grammar

def is_funcname(x):
    return isinstance(x, str) and len(x) == 3 and x.isalpha()

def is_varname(x):
    return isinstance(x, str) and len(x) in (1, 2) and x[0].isalpha()

def is_label(x):
    return isinstance(x, str) and x.startswith('"')

def is_relational(x):
    return isinstance(x, str) and x in('<', '=', '>', '<=', '<>', '>=')

def is_number(x):
    return isinstance(x, str) and x and x[0] in '.0123456789'

def statement():
    num = linenumber()
    typ = pop(is_stmt_type) or fail('unknown statement type')
    args = []
    for c in grammar[typ]:
        if callable(c):
            result = c()
            args.append(result)
        else:
            pop(c) or fail('expected ' + repr(c))
    return Stmt(num,typ, args)


def expression(prec = 1):
    exp = primary()
    while precedence(peek()) >= prec:
        op = pop()
        rhs = expression(precedence(op) + associativity(op))
        exp = Opcall(exp, op, rhs)
    return exp

def primary():
    
    if is_number(peek()):
        return number()
    elif is_varname(peek()):
        return variable()
    elif is_funcname(peek()):
        return Funcall(pop(), primary())
    elif pop('-'):
        return Funcall('NEG', primary())
    elif pop('('):
        exp = expression()
        pop(')') or fail('expected ")" to end expression')
        return exp
    else:
        return fail('unknown expression')
        



def precedence(op): 
    return (3 if op == '^' else 2 if op in ('*', '/') else 1 if op in ('+', '-') else 0)

def associativity(op):
    return (0 if op == '^' else 1)


def variable():
    V = varname()
    if pop('('):
        indexes = list_of(expression)()
        pop(')') or fail('expected ")" to close subscript')
        return Subscript(V, indexes)
    else:
        return V


class list_of:
    
    def __init__(self, category):
        self.category = category
    
    def __call__(self):
        result = ([self.category()] if tokens else [])
        while pop(','):
            result.append(self.category())
        return result


def fail(msg): raise SystemError(msg)


def labels_and_expressions():
    result = []
    while tokens:
        item = pop(is_label) or pop(',') or pop(';') or expression()
        result.append(item)
    return result



def Grammar():
    return {
        'LET': [variable, '=', expression],
        'READ': [list_of(variable)],
        'DATA': [list_of(number)],
        'PRINT': [labels_and_expressions],
        'GOTO': [linenumber],
        'IF': [expression, relational, expression, 'THEN', linenumber],
        'FOR': [varname, '=', expression, 'TO', expression, step],
        'NEXT': [varname],
        'END': [],
        'STOP': [],
        'DEF': [funcname, '(', varname, ')', '=', expression],
        'GOSUB': [linenumber],
        'RETURN': [],
        'DIM': [list_of(variable)],
        'REM': [anycharacters]
    }


grammar = Grammar()


def parse_line(line):
    
    global tokens
    tokens = tokennizer(line)
    try:
        stmt = statement()
        if tokens:
            fail('extra tokens at end of line')
        return stmt
    except SystemError as err:
        print("Error in line '{}' at '{}': {}".format(line, ' '.join(tokens), err))
        return Stmt(0, 'REM', [])


def parse(program):
    return sorted(map(parse_line, lines(program)))


class ExpressTest(unittest.TestCase):
    
    def parse(self, text, result, category = expression):
        global tokens
        tokens = tokennizer(text)
        return category() == result and not tokens

    def parse2(self, text, category = expression):
        global tokens
        tokens = tokennizer(text)
        return category()
    
    def test_parser(self):
        self.assertTrue(is_funcname('SIN') and is_funcname('FNZ'))
        self.assertTrue(not is_funcname('X') and not is_funcname(''))
        self.assertTrue(is_varname('X') and is_varname('A2'))
        self.assertTrue(not is_varname('FNZ') and not is_varname('A10') and not is_varname(''))
        self.assertTrue(is_relational('>') and is_relational('>=') and not is_relational('+'))

        self.assertTrue(self.parse('A + B * X + C',Opcall(Opcall('A', '+', Opcall('B', '*', 'X')), '+', 'C')))

        self.assertTrue(self.parse('A + B + C +  D', Opcall(Opcall(Opcall('A','+','B'), '+', 'C'),'+','D')))

        self.assertEqual(self.parse2('SIN(X)^2') ,Opcall(Funcall('SIN','X'), '^', 2))
        self.assertEqual(self.parse2('10 ^ 2 ^  3'), Opcall(10,'^', Opcall(2, '^',3)))
        self.assertEqual(self.parse2('A(I)+M(I, J)'), Opcall(Subscript('A',['I']), '+', Subscript('M',['I', 'J'])))

        self.assertEqual(self.parse2('X * -1'), Opcall('X', '*', Funcall('NEG',1)))

        self.assertEqual(self.parse2('X--Y--Z'), Opcall(Opcall('X', '-', Funcall('NEG', 'Y')), '-', Funcall('NEG', 'Z')))

        self.assertEqual(self.parse2('((((X))))'), 'X')




def preprocess(stmts):
    functions = {
        'SIN': math.sin, 'COS': math.cos, 'TAN': math.tan, 'ATN': math.atan, 
        'ABS': abs, 'EXP': math.exp, 'LOG': math.log, 'SQR': math.sqrt, 'INT': int,
        '>': op.gt, '<': op.lt, '=': op.eq, '>=': op.ge, '<=': op.le, '<>': op.ne, 
        '^': pow, '+': op.add, '-': op.sub, '*': op.mul, '/': op.truediv, 
        'RND': lambda _: random.random(), 'NEG': op.neg}
    
    data = deque()

    for (_, typ, args) in stmts:
        if typ == 'DEF':
            name, parm, body = args
            functions[name] = Function(parm, body)
        elif typ == 'DATA':
            data.extend(args[0])
    return functions, data



column = 0


def execute(stmts):
    
    global variables, functions, column
    functions, data = preprocess(stmts)
    variables = defaultdict(float)
    column = 0
    pc = 0
    ret = 0
    fors = {}
    goto = { stmt.num : i
            for (i, stmt) in enumerate(stmts)}
    
    while pc < len(stmts):
        (_, typ, args)  = stmts[pc]
        pc += 1
        if typ in ('END', 'STOP') or (type == 'READ' and not data):
            return
        elif typ == 'LET':
            V, exp = args
            let(V, evalu(exp))
        elif typ == 'READ':
            if not data : return
            for V in args[0]:
                let(V, data.popleft())  
        elif typ == 'PRINT':
            basic_print(args[0])
        elif typ == 'GOTO':
            pc = goto[args[0]]
        elif typ == 'IF':
            lhs, relational, rhs, dest = args
            if functions[relational](evalu(lhs), evalu(rhs)):
                pc = goto[dest]
        elif typ == 'FOR':
            V, start, end, step = args
            variables[V] = evalu(start)
            fors[V] = ForState(pc, evalu(end), evalu(step))
        elif typ == 'NEXT':
            V = args[0]
            continu, end, step = fors[V]
            if ((step >= 0 and variables[V] + step <= end) or
                (step < 0 and variables[V] + step >= end)):
                variables[V] += step
                pc = continu
        elif typ == 'GOSUB':
            ret = pc
            pc = goto[args[0]]
        elif typ == 'RETURN':
            pc = ret


def basic_print(items):
    
    for item in items:
        if item == ',': pad(15)
        elif item == ';': pad(3)
        elif is_label(item):
            print_string(item.replace('"', ''))
        else:
            print_string("{:g} ".format(evalu(item)))
    
    if (not items) or items[-1] not in (',', ';'):
        newline()


def pad(width):
    while column % width != 0:
        print_string(' ')
        

def print_string(s):
    
    global column
    print(s, end='')
    column += len(s)
    if column >= 75:
        newline()

def newline():
    global column
    print()
    column = 0


def run(pragram):
    execute(parse(pragram))



class runTest(unittest.TestCase):
    
    # def test_run1(self):
    #     run('''
    #     10 READ A1, A2, A3, A4
    #     15 LET D = A1 * A4 - A3 * A2
    #     20 IF D = 0 THEN 65
    #     30 READ B1, B2
    #     37   LET X1 = (B1*A4 - B2 * A2) / D
    #     42   LET X2 = ( A1 * B2 - A3 * B1)/D
    #     55   PRINT X1, X2
    #     60 GOTO 30
    #     65 PRINT "NO UNIQUE SOLUTION"
    #     70 DATA 1, 2, 4
    #     80 DATA 2, -7, 5
    #     85 DATA 1, 3, 4, -7
    #     90 END''')
    #     self.assertTrue(variables['D'] != 0)
    #     self.assertEqual(variables['X1'], -11/3)

    # def test_run2(self):
    #     run('''
    #     5 PRINT "X VALUE", "SINE", "RESOLUTION"
    #     10 READ D
    #     20   LET M = -1
    #     30   FOR X = 0 TO 3 STEP D
    #     40   IF SIN(X) <= M THEN 80
    #     50     LET X0 = X
    #     60     LET M = SIN(X)
    #     80   NEXT X
    #     85   PRINT X0, M, D
    #     90 GO TO 10
    #     95 DATA .1, .01, .001, .0001
    #     99 END
    #     ''')
    #     self.assertTrue(abs(variables['X0'] - math.pi / 2) < 0.00001)

    def test_run3(self):
        run('''
        10 FOR I = 1 TO 12
        20   PRINT I,
        30 NEXT I
        40 END''')
        self.assertEqual(variables['I'], 12)


if __name__ == '__main__':
    run('''
100 REM CONWAY'S GAME OF LIFE
102 REM G IS NUMBER OF GENERATIONS, M IS MATRIX SIZE (M X M)
104 REM A(X, Y) IS 1 IFF CELL AT (X, Y) IS LIVE
106 REM L(SELF_ALIVE, NEIGHBORS_ALIVE) IS 1 IFF CELL WITH THOSE COUNTS SHOULD LIVE ON
110 LET G = 10
120 LET M = 10
125 READ A(3,4), A(3,5), A(3,6), A(6,5), A(6,6), A(7,5), A(7,6)
130 DATA 1,      1,      1,      1,      1,      1,      1
140 READ L(0, 3), L(1, 3), L(1, 2)
145 DATA 1,       1,       1

150 REM MAIN LOOP: PRINT, THEN REPEAT G TIMES: UPDATE / COPY / PRINT
155 LET I = 0
160 GOSUB 700
170 FOR I = 1 TO G
180   GOSUB 300
190   GOSUB 500
200   GOSUB 700
210 NEXT I
220 STOP

300 REM SUBROUTINE: UPDATE B = NEXT_GENERATION(A)
310 FOR Y = 1 TO M
320   FOR X = 1 TO M
325     LET N = A(X-1,Y)+A(X+1,Y)+A(X,Y-1)+A(X,Y+1)+A(X-1,Y-1)+A(X+1,Y+1)+A(X-1,Y+1)+A(X+1,Y-1)
330     LET B(X, Y) = L(A(X, Y), N)
340   NEXT X
350 NEXT Y
360 RETURN

500 REM SUBROUTINE: COPY A = B
510 FOR Y = 1 TO M
520   FOR X = 1 TO M
530     LET A(X, Y) = B(X, Y)
540   NEXT X
550 NEXT Y
560 RETURN

700 REM SUBROUTINE: PRINT A
705 PRINT "        GENERATION " I
710 FOR Y = 1 TO M
720   FOR X = 1 TO M
730     IF A(X, Y) = 0 THEN 750
740       PRINT "O";
750     IF A(X, Y) = 1 THEN 770
760       PRINT ".";
770   NEXT X
780   PRINT
790 NEXT Y
795 RETURN

999 END 
''')
#     run('''
#  5 LET S = 0
# 10 LET N = 0
# 20 LET S = S + N/10
# 30   IF N >= 20 THEN 60
# 40   LET N = N + 1
# 50 GOTO 20
# 60 PRINT S
# 70 END
# ''')
#     run('''
# 100 LET X = 3
# 110 GOSUB 400
# 120 PRINT U, V, W
# 200 LET X = 5
# 210 GOSUB 400
# 215 PRINT U, V, W
# 220 LET Z = U + 2*V + 3*W
# 230 PRINT "Z = " Z
# 240 STOP
# 400 LET U = X*X
# 410 LET V = X*X*X
# 420 LET W = X*X*X*X + X*X*X + X*X + X
# 430 RETURN
# 440 END
# ''')
#     run('''
# 10  FOR I = 1 TO 3
# 20    READ P(I)
# 30  NEXT I
# 40  FOR I = 1 TO 3
# 50    FOR J = 1 TO 5
# 60      READ S(I, J)
# 70    NEXT J
# 80  NEXT I
# 90  FOR J = 1 TO 5
# 100   LET S = 0
# 110   FOR I = 1 TO 3
# 120     LET S = S + P(I) * S(I, J)
# 130   NEXT I
# 140   PRINT "TOTAL SALES FOR SALESMAN"J, "$"S
# 150 NEXT J
# 190 DIM S(3, 5)
# 200 DATA 1.25, 4.30, 2.50
# 210 DATA 40, 20, 37, 29, 42
# 220 DATA 10, 16, 3, 21, 8
# 230 DATA 35, 47, 29, 16, 33
# 300 END
# ''')
    # print(variables)
#     run('''
#  5 PRINT "D"; "SIN(D)", "COS(D)", "SIN(D)^2 + COS(D)^2"
# 20 LET P = 3.1415926535897932 / 180
# 30 FOR X = 0 TO 90 STEP 15
# 40   PRINT X; FNS(X), FNC(X), FNS(X)^2 + FNC(X)^2
# 50 NEXT X
# 97 DEF FNS(D) = SIN(D * P)
# 98 DEF FNC(D) = COS(D * P)
# 99 END
# ''')
#     run('''
# 10 FOR I = 1 TO 100
# 20   PRINT INT(10 * RND(X));
# 30 NEXT I
# 40 END
# ''')
    #  run('''
    #     10 FOR I = 1 TO 12
    #     20   PRINT I,
    #     30 NEXT I
    #     40 END''')
    # s = parse_line('20 IF D = 0 THEN 65')
    # print(s.args)
    # unittest.main()
    # print(parse(program))
    # print(program)
    # print(parse(program))
    # run(program)
    #  run('''
    #     10 READ A1, A2, A3, A4
    #     15 LET D = A1 * A4 - A3 * A2
    #     20 IF D = 0 THEN 65
    #     30 READ B1, B2
    #     37   LET X1 = (B1*A4 - B2 * A2) / D
    #     42   LET X2 = ( A1 * B2 - A3 * B1)/D
    #     55   PRINT X1, X2
    #     60 GOTO 30
    #     65 PRINT "NO UNIQUE SOLUTION"
    #     70 DATA 1, 2, 4
    #     80 DATA 2, -7, 5
    #     85 DATA 1, 3, 4, -7
    #     90 END''')

    # print(parse('''
    #     10 READ A1, A2, A3, A4
    #     15 LET D = A1 * A4 - A3 * A2
    #     20 IF D = 0 THEN 65
    #     30 READ B1, B2
    #     37   LET X1 = (B1*A4 - B2 * A2) / D
    #     42   LET X2 = ( A1 * B2 - A3 * B1)/D
    #     55   PRINT X1, X2
    #     60 GOTO 30
    #     65 PRINT "NO UNIQUE SOLUTION"
    #     70 DATA 1, 2, 4
    #     80 DATA 2, -7, 5
    #     85 DATA 1, 3, 4, -7
    #     90 END
    #     '''))

#     run('''
# 10 X = 1
# 20 GO TO JAIL
# 30 FOR I = 1 
# 40 IF X > 0 & X < 10 GOTO 999
# 50 LET Z = (Z + 1
# 60 PRINT "OH CANADA", EH?
# 70 LET Z = +3
# 80 LET X = Y ** 2
# 90 LET A(I = 1
# 100 IF A = 0 THEN 900 + 99
# 110 NEXT A(I)
# 120 DEF F(X) = X ^ 2 + 1
# 130 IF X != 0 THEN 999
# 140 DEF FNS(X + 2*P1) = SIN(X)
# 150 DEF FNY(M, B) = M * X + B
# 160 LET 3 = X
# 170 LET SIN = 7 * DEADLY
# 180 LET X = A-1(I)
# STOP
# 200 STOP IT, ALREADY
# 998 PRINT "PROGRAM STILL EXECUTES: 2 + 2 = " 2 + 2
# 999 END
# ''')





    


    