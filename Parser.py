import ply.yacc as yacc

from Lexer import tokens

precedence = (
    ('right', 'IDENTIFIER'),
)


def p_start(p):
    '''program : HAI EOL statement_list KTHXBYE EOL
               | HAI EOL statement_list KTHXBYE'''
    p[0] = p[3]


def p_statement_list(p):
    '''statement_list : statement_list statement EOL
                      | statement EOL'''
    if len(p) == 4:
        p[1].extend([p[2]])
        p[0] = p[1]
    else:
        p[0] = [p[1]]


def p_statement_empty(p):
    '''statement : '''


def p_statement(p):
    '''statement : expression'''
    p[0] = ['it', p[1]]


def p_statement_print(p):
    '''statement : VISIBLE expression'''
    p[0] = ['print', p[2]]


def p_statement_get(p):
    '''statement : GIMMEH IDENTIFIER'''
    p[0] = ['get', p[2]]


def p_statement_define(p):
    '''statement : I_HAS_A IDENTIFIER ITZ expression
                 | I_HAS_A IDENTIFIER'''
    if len(p) == 5:
        p[0] = ['define', p[2], p[4]]
    else:
        p[0] = ['declare', p[2]]


def p_statement_assign(p):
    '''statement : IDENTIFIER R expression'''
    p[0] = ['assign', p[1], p[3]]

def p_statement_convert(p):
    '''statement : IDENTIFIER IS_NOW_A TYPE'''
    p[0] = ['convert', p[1], p[3]]

def p_statement_if(p):
    '''statement : O_RLY EOL YA_RLY EOL statement_list NO_WAI EOL statement_list OIC
                 | O_RLY EOL YA_RLY EOL statement_list OIC'''
    if len(p) == 10:
        p[0] = ['if', p[5], p[8]]
    else:
        p[0] = ['if', p[5]]

def p_expression_list(p):
    '''expression_list : expression_list AN expression
                       | expression'''
    if len(p) == 4:
        p[1].extend([p[3]])
        p[0] = p[1]
    else:
        p[0] = [p[1]]

def p_expression_operator(p):
    '''expression : expression_unary_op
                  | expression_logic_op
                  | expression_binary_op
                  | expression_inf_arity_op'''
    p[0] = p[1]


def p_expression_unary_op(p):
    '''expression_unary_op : NOT expression'''
    p[0] = ['not', p[2]]

def p_expression_logic_op(p):
    '''expression_logic_op : BOTH_OF expression AN expression
                            | EITHER_OF expression AN expression
                            | WON_OF expression AN expression
                            | BOTH_SAEM expression AN expression
                            | DIFFRINT expression AN expression'''
    p[0] = ['logic',p[1],p[2],p[4]]

def p_expression_binary_op(p):
    '''expression_binary_op : SUM_OF expression AN expression
                            | DIFF_OF expression AN expression
                            | PRODUKT_OF expression AN expression
                            | QUOSHUNT_OF expression AN expression
                            | MOD_OF expression AN expression
                            | BIGGR_OF expression AN expression
                            | SMALLR_OF expression AN expression'''
    p[0] = ['OP',p[1],p[2],p[4]]


def p_expression_inf_arity_op(p):
    '''expression_inf_arity_op : ALL_OF expression_list MKAY
                               | ANY_OF expression_list MKAY'''
    p[0] = [p[1], p[2]]

def p_expression_variable(p):
    '''expression : YARN
                  | NUMBAR
                  | NUMBR
                  | TROOF
                  | variable'''
    p[0] = p[1]

def p_variable(p):
    '''variable : IDENTIFIER'''
    p[0] = ['value', p[1]]


def p_error(p):
    print('Unexpected token:', p)


parser = yacc.yacc()


