#!/usr/bin/env python3

import sys
import fileinput
import re

text = ""
for line in fileinput.input():
    text += line

#0. Quebras de página
#1. Separar pontuação das palavras
#2. Marcar capítulos
#3. Separar parágrafos de linhas pequenas
#4. Juntar linhas da mesma frase
#5. Uma frase por linha



#0. Quebras de página
regex_qp = r"(\n\n+)"
text = re.sub(regex_qp, r"\n\n#Page Break\n\n", text)


#2. Marcar capítulos
regex_cap = r".*(CAP[ÍI]TULO \w+).*"

text = re.sub(regex_cap, r"\n# \1", text)


#3. Separar parágrafos de linhas pequenas
regex_par = r"((.|\n)+?\.)\n"
text = re.sub(regex_par, r"§\1§", text)



#4. Juntar linhas da mesma frase
#regex_line = r"§(.|\n)+?§"
#text = re.sub(regex_line, r"\1", text)
#text = re.sub(regex_line, r"\n\3\n", text)





print(text)

#regex_nl = r"[a-z0-9,;–]\n\n[a-z0-9–]"
#text = re.sub(regex_nl, r"\1\n\2", text)


arr_poemas = []

def guarda_poema(poema):
    dic_poemas.append(poema)
    print(dic_poemas)
    return f"{len(dic_poemas)}"

#regex_poema = r"<poema>(.*?)</poema>"
#text = re.sub(regex_poema, guarda_poema, text, flag=re.S)

#print(text)



###TPC 
#Começar a fazer o TP
#avançar com a script