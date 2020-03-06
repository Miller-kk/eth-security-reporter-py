import json

def mythxParser():
    result = []
    newJson = {}
    with open('/eth-security-reporter-py/result_data/mythx.json') as json_file:
        json_data = json.load(json_file)
        for data in json_data[0]["issues"]:
            if(data["swcTitle"] != ''):
                newJson["name"] = data["swcTitle"]
                newJson["description"] = data["description"]["head"]
                newJson["impact"] = data["severity"]
                newJson["lines"] = data["decodedLocations"]
                result.append(newJson)
                newJson = {}
        return result