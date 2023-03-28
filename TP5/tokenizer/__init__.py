#! /usr/bin/env python3
"""Module to tokenize books
"""

__version__ = '0.5'

import re
import sys
import fileinput
import argparse

def guarda_poema(poema):
        arr_poemas = []
        arr_poemas.append(poema[1]) # vai buscar o grupo 1
        #return f">>{len(arr_poemas)}<<"
        return f">>{len(arr_poemas)}<<"


abreviaturas = {}
def guarda_abreviaturas(abrev):
    if abrev[0] in abreviaturas.keys():
        abreviaturas[abrev[0]] = abreviaturas[abrev[0]] + 1
    else:
        abreviaturas[abrev[0]] = 1
    return f"<<{abrev[1]}>>"

def tokenizer():

    parser = argparse.ArgumentParser(description='Process input and output file names.')
    parser.add_argument('fileIn', type=str, help='Input file name')
    parser.add_argument('fileOut', type=str, help='Output file name')
    args = parser.parse_args()

        
    fileIn = args.fileIn
    fileOut = args.fileOut


    with open(fileIn, 'r') as f:
        lines = f.readlines()

    txt = ""
    for line in lines:
        txt += line
    #txt = ""
    #for line in fileinput.input():
        #txt += line

    regex_cap = r".*(CAP[ÍI]TULO\s+\w+).*"
    txt = re.sub(regex_cap, r"\n# \1", txt)


    regex_nl = r"([a-z0-9,;-])\n\n([a-z0-9])"
    txt = re.sub(regex_nl, r"\1\n\2", txt)

    

    regex_poema = r"<poema>(.*?)</poema>"
    txt = re.sub(regex_poema, guarda_poema, txt, flags=re.S)

    regex_abreviaturas = r"([sS][rR][tT]?[aA]?[sS]?)\."
    txt = re.sub(regex_abreviaturas, guarda_abreviaturas, txt, flags=re.S)


    regex_ponto = r"\. ?"
    txt = re.sub(regex_ponto, r".\n", txt, flags=re.S)

    regex_quebra = r"([^\n])\n+"
    txt = re.sub(regex_quebra, r"\1\n", txt, flags=re.S)

    regex_reticencias = r"\.\n\.\n\.\n"
    txt = re.sub(regex_reticencias, r"...\n", txt, flags=re.S)

    regex_frases = r"([^\n])\n([^A-Z])"
    txt = re.sub(regex_frases, r"\1 \2", txt, flags=re.S) # 1 frase por linha
    # não exatamente a 100% porque existem uns nomes próprios que começam com letra maiscula
    # esses teriam de ser tratados à parte



    with open(fileOut, 'w') as f:
        f.write(txt)
    # print(arr_poemas)
    # print(abreviaturas)
    # print(paragrafos)

    # 1 Separar pontuacao das palavras
    # 2 Marcar capitulos [DONE]
    # 3 Separar paragrafos de linhas pequenas
    # 4 Juntar linhas da mesma frase
    # 5 Uma frase por linha
    # 6 Quebras de página [DONE]
    # 7 Marcar poemas [DONE]
    # 8 Guardar abreviaturas: Sr., Sra., etc. [DONE]