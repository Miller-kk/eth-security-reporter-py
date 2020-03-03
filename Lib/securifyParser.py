import json

def securifyParser():
    result = []
    newJson = {}
    with open('./result_data/securify.json') as json_file:
        json_data = json.load(json_file)
        for contractName in json_data.keys():
           for bugName in json_data[contractName]["results"].keys():
               if(len(json_data[contractName]["results"][bugName]["violations"]) > 0):
                    newJson["name"] = bugName
                    newJson["description"] = bugName
                    newJson["impact"] = ''
                    newJson["lines"] = json_data[contractName]["results"][bugName]["violations"]
                    result.append(newJson)
                    newJson = {}
        return result