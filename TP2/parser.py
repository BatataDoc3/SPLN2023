import ply.yacc as yacc

def p_1(p): 
    "dic: Es"

def p_2(p): 
    "Es: E LINHA_B Es"

def p_3(p): 
    "Es: E" 

def p_4(p): 
    "E: ITEMS"

def p_5(p): 
    "ITEMS: ITEM '\n' ITEMS"

def p_6(p): 
    "ITEMS: ITEM"

def p_7(p): 
    "ITEM: AT_CONC"

def p_8(p): 
    "ITEM: LING"

def p_9(p): 
    "AT_CONC: ID ':' VAL"

def p_10(p): 
    "LING: ID_LING ':' '\n' TS"

def p_11(p): 
    "TS: TS T"

def p_12(p): 
    "TS: T"

def p_13(p): 
    "T: '-' VAL AT_TS"

def p_14(p): 
    "AT_TS: AT_TS AT_T"

def p_15(p): 
    "AT_TS: "

def p_16(p): 
    "AT_T: '\n' '+' ID ':' VAL"