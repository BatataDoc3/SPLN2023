'''
Conc = Conceito
'''


import ply.yacc as yacc

def p_dic(p): 
    "dic: Es"

def p_Es(p): 
    "Es: E LINHA_B Es"

def p_Es_E(p): 
    "Es: E" 

def p_E(p): 
    "E: ITEMS"

def p_ITEMS(p): 
    "ITEMS: ITEM '\n' ITEMS"

def p_ITEMS_ITEM(p): 
    "ITEMS: ITEM"

def p_ITEM_AT_CONC(p): 
    "ITEM: AT_CONC"

def p_ITEM_LING(p): 
    "ITEM: LING"

def p_AT_CONC(p): 
    "AT_CONC: ID ':' VAL"

def p_LING(p): 
    "LING: ID_LING ':' '\n' TS"

def p_TS(p): 
    "TS: TS T"

def p_TS_T(p): 
    "TS: T"

def p_T(p): 
    "T: '-' VAL AT_TS"

def p_AT_TS(p): 
    "AT_TS: AT_TS AT_T"

def p_AT_TS_vazio(p): 
    "AT_TS: "

def p_AT_T(p): 
    "AT_T: '\n' '+' ID ':' VAL"


