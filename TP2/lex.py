import ply.lex as lex

literals = [':', '-', '+', '\n']

tokens = ('ID', 'ID_LING', 'VAL', 'LINHA_B')

def t_ID(t): 
    r'\w+(?= *:)'
    
def t_ID_LING(t):
    r'[es, en, pt, la]'

def t_LINHA_B(t):
    r'\s+'

def t_VAL(t):
    r'.+\n'