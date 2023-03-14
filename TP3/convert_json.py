###########################################HTML#############################################################


from json2html import *

f = open("medicina_treated.json", "r")
data = f.read()


html = open("medicina_html.html", "w")

html.write(json2html.convert(json = data))



###########################################Latex#############################################################


#import json2latex


#with open('medicina_tatex.tex', 'w') as ff:
#    json2latex.dump('data', data, ff)



###########################################MD#############################################################


markdown = ""
if isinstance(data, dict):
    for key, value in data.items():
        if isinstance(value, dict):
            markdown += f"\n## {key}\n"
            markdown += generate_markdown(value)
        elif isinstance(value, list):
            markdown += f"\n### {key}\n"
            for item in value:
                markdown += generate_markdown(item)
        else:
            markdown += f"\n**{key}:** {value}\n"
else:
    markdown += f"\n{data}\n"

fff = open("medicina_md.md", "w")
fff.write(markdown)





import pandas as pd
import csv

df = pd.read_json(data)

df.to_csv('medicina_csv.csv')