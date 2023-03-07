import ply.lex as lex

literals = [':']

tokens = ('TAB', 'NEWLINE', 'ID', 'NUMBER', 'ID_NOME', 'NOME', 'ID_GENERO', 'GENERO', 'ID_AREAS', 'AREAS', 'ID_SIN', 'TEXTO', 'ID_LINGUAS', 'ID_LINGUA', 'ID_NOTAS')

def t_TAB(t):
    r'\t'

def t_NEWLINE(t):
    r'\n'

def t_ID(t):
    r'ID:'

def t_NUMBER(t):
    r'\d+'

def t_ID_NOME(t):
    r'NOME'

def t_NOME(t):
    r'\w+'

def t_ID_GENERO(t):
    r'GENERO'

def t_GENERO(t):
    r'[m,f,a]'

def t_ID_AREAS(t):
    r'AREAS'

def t_AREAS(t):
    r'\w+[\,,w]+'

def t_ID_SIN(t):
    r'SIN'

def t_TEXTO(t):
    r'.+'

def t_ID_LINGUAS(t):
    r'LINGUAS'

def t_ID_LINGUA(t):
    r'[es,en,pt,la]'

def t_ID_NOTAS(t):
    r'NOTA'


lexer = lex.lex()