import json
from json2html import *

def prettyPrint(tool, infoArray):
    print("\n\n########################################"+tool+" Result########################################\n")
    if(infoArray == ''):
        print("error - " +tool)
    else:
        for info in infoArray:
            print("===============================================================================")
            print("Name: " + info["name"])
            print("description: " + info["description"])
            print("impact: " + info["impact"])
            for line in info["lines"]:
                print("lines: " + str(line))

def stringTofile(output,tool):
    f =open("./result_data/"+tool, 'w')

    if(type(output) == bytes):
        f.write(output[:-1].decode())
    else:
        f.write(str(output))


def createTable(resultArray):
    tableHtml = json2html.convert(json = resultArray)
    print(tableHtml)
    stringTofile(resultArray,"total.html")