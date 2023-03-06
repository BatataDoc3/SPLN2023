import ply.yacc as yacc

from mylex import tokens, literals


def p_es(p):
    "Es : Id Nome Genero Areas Sin Linguas Notas"
    print("1")

def p_Id(p):
    "Id : ID ':' NUMBER"
    print("2")

def p_Nome(p):
    "Nome : ID_NOME ':' NOME"
    print("3")

def p_Genero(p):
    "Genero : ID_GENERO ':' GENERO"
    print("4")

def p_Areas(p):
    "Areas : ID_AREAS ':' AREAS"
    print("5")


def p_Sin(p):
    "Sin : ID_SIN ':' TEXTO"
    print("6")


def p_Sin_vazio(p):
    "Sin : "
    print("7")


def p_Linguas(p):
    "Linguas : ID_LINGUAS ':' NEWLINE Lingua"


def p_Lingua(p):
    "Lingua : TAB ID_LINGUA NOME NEWLINE Lingua"

def p_Lingua_vazio(p):
    "Lingua : "
    print("10")

def p_Notas(p):
    "Notas : ID_NOTAS ':' TEXTO"
    print("11")

def p_Notas_vazio(p):
    "Notas : "
    print("12")


parser = yacc.yacc()

with open('example.txt', 'r') as f:
    content = f.read()
    print(content)
    parser.success = True
    parser.flag = True
    parser.parse(content)