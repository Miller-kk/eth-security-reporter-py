import json
import prettyPrint as pp

def smartcheckParser():
    result = []
    newJson = {}
    readData = open('/eth-security-reporter-py/result_data/smartcheck').read().split("\n")
    for data in readData:
        if("ruleId" in data):
            ruleParse = data.split(" ")
            newJson = {}
            newJson["name"] = ruleParse[len(ruleParse) -1]
        elif("severity" in data):
            secerityParse = data.split(" ")
            newJson["impact"] = secerityParse[len(secerityParse) - 1] 
        elif("line" in data):
            lineParse = data.split(" ")
            newJson["lines"] = lineParse[len(lineParse) - 1]
        elif("content" in data):
            contentParse = data.split(" ")
            newJson["description"] = contentParse[len(contentParse) -1]
            result.append(newJson)
    print(result)
    return result