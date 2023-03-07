import ply.yacc as yacc

from mylex import tokens, literals


def p_dic(p):
    "Dic : Entradas"
    print("1")

def p_entradas(p):
    "Entradas : Es Entradas"
    print("2")

def p_entradas_ultimo(p):
    "Entradas : Es"
    print("3")

def p_es(p):
    "Es : Id Nome Genero Areas Sin Linguas Notas"
    print(p[1])
    print("4")

def p_es_vazio(p):
    "Es : "
    print("5")

def p_Id(p):
    "Id : ID NUMBER NEWLINE"
    print(p[1])
    print("6")


def p_Nome(p):
    "Nome : ID_NOME ':' NOME NEWLINE"
    print(p[1])
    print("6")


def p_Genero(p):
    "Genero : ID_GENERO ':' GENERO NEWLINE"
    print(p[1])
    print("7")

def p_Areas(p):
    "Areas : ID_AREAS ':' AREAS NEWLINE"
    print(p[1])
    print("8")


def p_Sin(p):
    "Sin : ID_SIN ':' TEXTO NEWLINE"
    print(p[1])
    print("9")


def p_Sin_vazio(p):
    "Sin : "
    print("10")


def p_Linguas(p):
    "Linguas : ID_LINGUAS ':' NEWLINE Lingua"
    print(p[1])
    print("11")


def p_Lingua(p):
    "Lingua : TAB ID_LINGUA NOME NEWLINE Lingua"
    print(p[2])
    print("12")

def p_Lingua_vazio(p):
    "Lingua : "
    print("13")

def p_Notas(p):
    "Notas : ID_NOTAS ':' TEXTO NEWLINE"
    print(p[1])
    print("14")

def p_Notas_vazio(p):
    "Notas : "
    print("15")

def p_error(p):
    print('Erro sintático: ', p)
    parser.success = False


parser = yacc.yacc()

with open('example.txt', 'r') as f:
    content = f.read()
    print(content)
    parser.success = True
    parser.flag = True
    parser.parse(content)