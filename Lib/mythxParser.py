import json

def mythxParser():
    result = []
    newJson = {}
    with open('./result_data/mythx.json') as json_file:
        json_data = json.loads(json_file)
        for data in json_data[0][0]["issues"]:
            if(data["swcTitle"] != ''):
                newJson["name"] = data["swcTitle"]
                newJson["description"] = data["description"]["head"]
                newJson["impact"] = data["severity"]
                newJson["lines"] = data["decodedLocations"]
                result.append(newJson)
                newJson = {}
        return result