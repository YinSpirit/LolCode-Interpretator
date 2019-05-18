import ply.lex as lex

tokens = ('I_HAS_A','ITZ', 'HAI', 'OIC','IS_NOW_A',
          'R', 'YARN','NUMBR','NUMBAR', 'TROOF',
          'EOL', 'AN', 'SUM_OF','DIFF_OF','PRODUKT_OF',
          'QUOSHUNT_OF','MOD_OF','BIGGR_OF',
          'SMALLR_OF', 'BOTH_OF','EITHER_OF','WON_OF',
          'NOT','ALL_OF', 'ANY_OF', 'BOTH_SAEM',
          'DIFFRINT', 'MKAY','VISIBLE', 'GIMMEH', 'O_RLY',
          'YA_RLY','NO_WAI','KTHXBYE', 'IDENTIFIER','TYPE')

def t_I_HAS_A(t):
    r'I\s+HAS\s+A\b'
    t.value = 'I_HAS_A'
    return t

def t_ITZ(t):
    r'ITZ'
    return t

def t_R(t):
    r'\bR\b'
    return t

def t_VISIBLE(t):
    r'VISIBLE'
    return t

def t_GIMMEH(t):
    r'GIMMEH'
    return t

def t_SUM_OF(t):
    r'SUM\ OF'
    return t

def t_DIFF_OF(t):
    r'DIFF\ OF'
    return t

def t_PRODUKT_OF(t):
    r'PRODUKT\ OF'
    return t

def t_QUOSHUNT_OF(t):
    r'QUOSHUNT\ OF'
    return t

def t_MOD_OF(t):
    r'MOD\ OF'
    return t

def t_BIGGR_OF(t):
    r'BIGGR\ OF'
    return t

def t_SMALLR_OF(t):
    r'SMALLR\ OF'
    return t

def t_BOTH_OF(t):
    r'BOTH\ OF'
    return t

def t_EITHER_OF(t):
    r'EITHER\ OF'
    return t

def t_WON_OF(t):
    r'WON\ OF'
    return t

def t_NOT(t):
    r'NOT'
    return t

def t_ALL_OF(t):
    r'ALL\ OF'
    return t

def t_MKAY(t):
    r'MKAY'
    return t

def t_BOTH_SAEM(t):
    r'BOTH\ SAEM'
    return t

def t_DIFFRINT(t):
    r'DIFFRINT'
    return t

def t_O_RLY(t):
    r'O\ RLY\?'
    return t

def t_YA_RLY(t):
    r'YA\ RLY'
    return t

def t_NO_WAI(t):
    r'NO\ WAI'
    return t

def t_HAI(t):
    r'HAI'
    return t

def t_KTHXBYE(t):
    r'KTHXBYE'
    return t

def t_AN(t):
    r'\bAN\b'
    return t

def t_IS_NOW_A(t):
    r'IS\s+NOW\s+A\b'
    return t

def t_OIC(t):
    r'OIC'
    return t

def t_ANY_OF(t):
    r'ANY\ OF'
    return t

def t_NUMBR(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_NUMBAR(t):
    r'[+-]?[0-9]+[.][0-9]*'
    t.value = float(t.value)
    return t


def t_YARN(t):
    r'\"[^"]*\"'
    t.value = str(t.value[1:-1])
    return t


def t_TROOF(t):
    r'WIN|FAIL'
    t.value = True if (t.value == "WIN") else False
    return t


def t_EOL(t):
    r'\n+'
    t.lexer.lineno += 1
    return t

def t_comment(t):
    r'BTW[^\n]*'
    pass

def t_TYPE(t):
    r'NUMBR|NUMBAR|YARN|TROOF'
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = 'IDENTIFIER'
    return t


t_ignore = ' \t'


def t_error(t):
    print("Illegal character '%s' at line %d" % (t.value[0], t.lexer.lineno))
    t.lexer.skip(1)



lexer = lex.lex()

# data =''''''
#
# lexer.input(data)
#
# while True:
#     tok = lexer.token()
#     if not tok: break
#     print(tok)
